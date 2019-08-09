

tmux detach

cat list_subjects.txt | xargs -n 1 -P 32 ../fast_script


bet X brain.nii.gz

fast brain


echo "extract volume for WM"
result=$(fslstats WM_MT_90 -V)
echo "$subj "WM" $result" >> $outDir/WM_volume.txt
