Dataset organize

Clone https://github.com/ifzhang/ByteTrack
Replace configs/datasets/mot.yml with ...

With ground truth
python -u tools/demo_track.py image -f exps/example/mot/yolox_x_soccernet.py -c pretrained/bytetrack_x_mot20.tar --fp16 --fuse --match_thresh 0.7 --save_result --path /mnt/storage/gait-0/xin/dataset/Soccernet-v2_tracking/test/$file/img1


Without ground truth
python tools/track.py -f exps/example/mot/yolox_x_soccernet.py -c pretrained/bytetrack_x_mot20.tar -b 1 -d 1 --fp16 --fuse --match_thresh 0.8 --mot20


