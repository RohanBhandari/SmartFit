#!/bin/bash

# Setup environment
conda create -y --name smartfit python=2.7 pip
source activate smartfit
pip install -r requirements.txt

# Clone repository for human parsing
git clone https://github.com/RohanBhandari/LIP_JPPNet.git ./human_parsing/LIP_JPPNet/
mkdir ./human_parsing/LIP_JPPNet/checkpoint/
cd ./human_parsing/LIP_JPPNet/checkpoint/
printf "\nDownloading human parsing model. This may take a few minutes.\n\n"
curl -L -o human_parsing_model.zip https://www.dropbox.com/sh/b54kk4asq9f3bgw/AADHgr29Hj-rystQCj1OFTmra\?dl\=1
unzip human_parsing_model.zip
cd ../../..

# Clone repository for pose estimation
git clone https://github.com/RohanBhandari/keras_Realtime_Multi-Person_Pose_Estimation.git ./pose_estimation/keras_Realtime_MultiPerson_Pose_Estimation
printf "\nDownloading pose estimation model. This may take a few minutes.\n\n"
mkdir pose_estimation/keras_Realtime_MultiPerson_Pose_Estimation/model/keras/
cd pose_estimation/keras_Realtime_MultiPerson_Pose_Estimation/model/keras/
curl -L -o model.h5 https://www.dropbox.com/s/llpxd14is7gyj0z/model.h5
cd ../../../..

# Clone repository for try-on
git clone https://github.com/RohanBhandari/VITON.git ./try-on/VITON/
cd try-on/VITON/
git checkout f8427292e653df9ecb09a1413cfc4e0575a34469 # Get specific commit of repo
cd model/
printf "\nDownloading clothing transfer models. This may take a few minutes.\n\n"
curl -L -o clothing_transfer_public_models.zip https://www.dropbox.com/sh/bxl1omic7o2yf4y/AABpnCFbh1Vr6W-xJqS8rGvqa\?dl\=1
unzip clothing_transfer_public_models.zip
cd ../../..
