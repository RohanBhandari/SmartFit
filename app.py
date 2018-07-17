from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

# Run inference
@app.route('/api/infer', methods=['POST'])
def infer():
    # Check that the post contains the right fields
    if not all(i in request.files for i in ['person', 'clothing']):
        return jsonify(error = 'Incorrect payload!')

    # Check that the files are images
    if not (request.files['person'].mimetype[:5] == request.files['clothing'].mimetype[:5] == "image"):    
        return jsonify(error = 'Inputs must be images!')

    # Handle data and execute inference
    person_img = request.files['person']
    clothing_img = request.files['clothing']

    person_img.save('./inputs/input_person.jpg')
    clothing_img.save('./inputs/input_clothing.jpg')

    os.system('./run_smartfit.sh ./inputs/input_person.jpg ./inputs/input_clothing.jpg')

    # Check that files exists (i.e. smartfit didn't crash)
    if not os.path.isfile('output/output.png'):
        return jsonify(error = '500: Internal server error')

    return send_from_directory('./output/', 'output.png')


if __name__ == '__main__':
    app.run(debug=True)
