Clone https://github.com/ifzhang/ByteTrack into the current folder

Get data into 
Download pretrained weights

copy demo_track.py into tools/demo_track.py
copy yolox_x_soccernet.py into exps/example/mot/

With ground truth

arrange ground truth into ... '/../det/det.txt'

python tools/demo_track.py image -f exps/example/mot/yolox_x_soccernet.py -c pretrained/bytetrack_x_mot20.tar --fp16 --fuse --match_thresh 0.8 \
--save_result --path /mnt/storage/gait-0/xin/dataset/Soccernet-v2_tracking/test/$file/img1

Without ground truth
set self.inference_with_ground_truth in exps/example/mot/yolox_x_soccernet.py to False
python tools/track.py -f exps/example/mot/yolox_x_soccernet.py -c pretrained/bytetrack_x_mot20.tar -b 1 -d 1 --fp16 --fuse --match_thresh 0.8 --mot20

/mnt/storage/gait-0/Multimodal_sports_datasets/SoccerNet-v2_temp/tracking

zip results:
soccernet_mot_results.zip

Tested on linux version