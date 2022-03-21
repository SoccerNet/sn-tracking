### Prerequisite
Make sure CUDA and CUDNN are properly installed and related environment variables are properly set. 
Verified versions are anaconda3-5.1.0 + CUDA 10.0.130 + CUDNN 7.6.5 on Ubuntu 20.04.3 LTS. 

### Obtain ByteTrack code
Follow ByteTrack instructions to [Installing on the host machine](https://github.com/ifzhang/ByteTrack#1-installing-on-the-host-machine)
Let the source folder be. <ByteTrack_HOME>
Download bytetrack_x_mot20 pretrained model from the same page and put it in <ByteTrack_HOME>/pretrained.

### Download this repo and replace a few files in ByteTrack
```
    git clone https://github.com/SoccerNet/sn-tracking.git  SN_TRACKING_HOME
```

Download soccernet data and extract
Move data into dataset/SN_tracking

### Update Bytetrack code for Soccernet tracking
```
    cp -i demo_track.py <ByteTrack_HOME>/tools/demo_track.py
    cp -i yolox_x_soccernet.py <ByteTrack_HOME>/exps/example/mot/
    cp run_bytetrack_gt_batch.sh <ByteTrack_HOME>
    cp tools/evaluate_soccernet_v3_tracking.py <ByteTrack_HOME>
```

### Run inference for each sequence
```
    export ByteTrack_HOME=<ByteTrack_HOME>
    cd <ByteTrack_HOME>
    bash run_bytetrack_gt_batch.sh
```

### Zip and generate results for evaluation online
```
    zip soccernet_mot_results.zip <RESULT_FOLDER>/SNMOT-???.txt
```
The generated soccernet_mot_results.zip can be submitted to the evaluation server.

### Evaluate locally



With ground truth

arrange ground truth into ... '/../det/det.txt'

python tools/demo_track.py image -f exps/example/mot/yolox_x_soccernet.py -c pretrained/bytetrack_x_mot20.tar --fp16 --fuse --match_thresh 0.8 \
--save_result --path /mnt/storage/gait-0/xin/dataset/Soccernet-v2_tracking/test/$file/img1

zip results:
zip soccernet_mot_results.zip <RESULT_FOLDER>/SNMOT-???.txt

