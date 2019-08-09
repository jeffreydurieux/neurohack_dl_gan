

tmux detach

ls /data/ | xargs -n 1 -P 32 ./1_preprocess_niftified_pngs.sh


ls | xargs -n 1 -P 32 " bet $1 "$1"_brain "

bet X brain.nii.gz

fast brain


echo "extract volume for WM"
result=$(fslstats WM_MT_90 -V)
echo "$subj "WM" $result" >> $outDir/WM_volume.txt
