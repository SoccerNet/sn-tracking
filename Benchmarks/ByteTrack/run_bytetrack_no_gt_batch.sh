for file in $ByteTrack_HOME/tracking-2023/$SN_TRACKING_MODE/*/ ; do 
file="${file%/}" # strip trailing slash
file="${file##*/}"
# echo "$file is the directoryname without slashes"
python tools/demo_track_no_gt.py image -f exps/example/mot/yolox_x_soccernet_no_gt.py \
-c pretrained/bytetrack_x_mot20.tar --fp16 --fuse --save_result \
--path $ByteTrack_HOME/tracking-2023/$SN_TRACKING_MODE/$file/img1
done
