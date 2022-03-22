### Prerequisite
Make sure CUDA and CUDNN are properly installed and related environment variables are properly set. 
Verified versions are anaconda3-5.1.0 + CUDA 10.0.130 + CUDNN 7.6.5 on Ubuntu 20.04.3 LTS. 

### Obtain ByteTrack code
Follow ByteTrack instructions to [Installing on the host machine](https://github.com/ifzhang/ByteTrack#1-installing-on-the-host-machine).
Let the source folder be <ByteTrack_HOME>.
Download bytetrack_x_mot20 pretrained model from the same page and put it in <ByteTrack_HOME>/pretrained.

### Download this repo and replace a few files in ByteTrack
```
    git clone https://github.com/SoccerNet/sn-tracking.git  SN_TRACKING_HOME
    pip install SoccerNet

```
Go into SN_TRACKING_HOME
```
    python tools/download_data.py
```
The data will be saved in SN_TRACKING_HOME.

### Update Bytetrack code for Soccernet tracking
```
    cd <SN_TRACKING_HOME>/Benchmarks/ByteTrack
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
    export SN_TRACKING_MODE=test
```
To run challenge:
```
export SN_TRACKING_MODE=challenge
```

### Zip and generate results for evaluation online
```
    cd <RESULT_FOLDER>
    zip soccernet_mot_results.zip SNMOT-???.txt
```
The generated soccernet_mot_results.zip can be submitted to the evaluation server.

### Evaluate locally

```
pip install git+https://github.com/JonathonLuiten/TrackEval.git

python tools/evaluate_soccernet_v3_tracking.py --BENCHMARK SNMOT --DO_PREPROC False --SEQMAP_FILE tools/SNMOT-test.txt --TRACKERS_TO_EVAL test --SPLIT_TO_EVAL test --OUTPUT_SUB_FOLDER eval_results --TRACKERS_FOLDER_ZIP soccernet_mot_results.zip --GT_FOLDER_ZIP gt.zip  
```


