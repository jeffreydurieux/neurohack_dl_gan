set -x
subj=$1

dataDir=/home/ubuntu/data/reconstructed_nifti/analysis_young/"$subj"_derivative

echo "extract volume for WM"
result1=$(fslstats $dataDir/pv1_volume -V)
echo "$subj "CSF" $result1" >> $outDir/CSF_volume.txt

echo "extract volume for WM"
result2=$(fslstats $dataDir/WM_MT_90 -V)
echo "$subj "WM" $result2" >> $outDir/WM_volume.txt

echo "extract volume for WM"
result3=$(fslstats $dataDir/WM_MT_90 -V)
echo "$subj "GM" $result3" >> $outDir/GM_volume.txt
