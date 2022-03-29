### Prerequisite
Make sure CUDA and CUDNN are properly installed and related environment variables are properly set. Verified versions are CUDA 10.2 + CUDNN 7.6.5 on Ubuntu 20.04. (Do not use CUDA 10.2 + CUDNN 8, because it may cause seg fault in training some tracking models)

### Create virtual environment
```
    conda create -n paddle_soccernet python=3.8
    conda activate paddle_soccernet
```

### Install PaddlePaddle
Install PaddlePaddle according to its [instructions](https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.3/docs/tutorials/INSTALL.md), for example:
```    
    python -m pip install paddlepaddle-gpu==2.2.2
```

### Download PaddleDetection
Download the verified branch (release/2.3) of PaddleDetection to a directory, denoted as PADDLE_DETECTION_ROOT, and run
```
    git clone -b release/2.3 https://github.com/PaddlePaddle/PaddleDetection.git  PADDLE_DETECTION_ROOT
```
Then follow the [instructions](https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.3/docs/tutorials/INSTALL.md#2-install-paddledetection) to install dependencies for PaddleDetection.

### Download this repo and copy a few files into PaddleDetection 
Download this repo to a directory, denoted as SN_TRACKING_ROOT, and run
```
    git clone https://github.com/SoccerNet/sn-tracking.git  SN_TRACKING_ROOT
    cp -r SN_TRACKING_ROOT/Benchmarks/DeepSORT/configs  PADDLE_DETECTION_ROOT/
    cp -r SN_TRACKING_ROOT/Benchmarks/DeepSORT/dataset/mot/*.py  PADDLE_DETECTION_ROOT/dataset/mot/
```

### Prepare the data into a unified format
If you have not downloaded the dataset, follow the root level [readme](https://github.com/SoccerNet/sn-tracking#how-to-download-soccernet-tracking) to download (and unzip) the SoccerNet-tracking dataset. Denote the path of the dataset root directory as SN_TRACKING_DATA_ROOT, and run the following commands
```
    mkdir PADDLE_DETECTION_ROOT/dataset/mot/{image_lists,SN}
    ln -s SN_TRACKING_DATA_ROOT PADDLE_DETECTION_ROOT/dataset/mot/SN/images

    cd PADDLE_DETECTION_ROOT/dataset/mot/
    python gen_image_list_SN.py
    python gen_labels_SN.py
    python gen_det_results_SN.py
```
After running above commands, image lists will be generated under PADDLE_DETECTION_ROOT/dataset/mot/image_lists, labels will be generated under PADDLE_DETECTION_ROOT/dataset/mot/SN/labels_with_ids, and gt bboxes as detections will be generated under PADDLE_DETECTION_ROOT/dataset/mot/SN/det_files. This step is meet the [data format](https://github.com/PaddlePaddle/PaddleDetection/blob/release/2.3/configs/mot/README_en.md#data-format) requirements of PaddleDetection.

### Run inference with a pretrained model
Let INFERENCE_OUTPUT_TEST denote the output directory you want the results to save to.
```
    cd PADDLE_DETECTION_ROOT
    python tools/eval_mot.py -c configs/mot/deepsort/reid/deepsort_pcb_pyramid_r101_sn.yml --det_results_dir dataset/mot/SN/det_files/test/  --output_dir INFERENCE_OUTPUT_TEST/
```
A pretrained model specified by deepsort_pcb_pyramid_r101_sn.yml will be downloaded and run on the test set. Note that gt bboxes are fed in as detection results. The inference output will be saved to INFERENCE_OUTPUT. Note that a broken evaluation is also run at the end, please ignore the broken evaluation print-out at this step. 

To run the inference on the challenge set, simply change the value of "data_root" under "EvalMOTDataset" section in the config file and feed in the gt detections for the challenge set. Or you can directly run the following command:
```
    python tools/eval_mot.py -c configs/mot/deepsort/reid/deepsort_pcb_pyramid_r101_sn_challenge.yml --det_results_dir dataset/mot/SN/det_files/challenge/  --output_dir INFERENCE_OUTPUT_CHALLENGE/
```

### Evaluation
To run the evaluation, zip the inference output with the following commands. Then you can evaluate the performance locally or submit the zip file to the eval server. 
```
    cd INFERENCE_OUTPUT_TEST/mot_results
    zip soccernet_mot_results.zip *.txt
```

To evaluate locally, you need to zip the ground truth txt files to get a gt.zip file.
```
    cd SN_TRACKING_ROOT
    python tools/zip_gt.py -f SN_TRACKING_DATA_ROOT/test/
```

Run the following to evaluate on the test set locally:
```
    pip install git+https://github.com/JonathonLuiten/TrackEval.git
    cd SN_TRACKING_ROOT
    python tools/evaluate_soccernet_v3_tracking.py --BENCHMARK SNMOT --DO_PREPROC False --SEQMAP_FILE tools/SNMOT-test.txt --TRACKERS_TO_EVAL test --SPLIT_TO_EVAL test --OUTPUT_SUB_FOLDER eval_results --TRACKERS_FOLDER_ZIP soccernet_mot_results.zip --GT_FOLDER_ZIP gt.zip
```
It is expected to achieve a HOTA score of 69.55 on the test set.
