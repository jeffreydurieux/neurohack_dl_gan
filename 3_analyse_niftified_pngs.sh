set -x
subj=$1

dataDir=/data/"$subj"_derivative

echo "extract volume for CSF"
result1=$(fslstats $dataDir/"$subj".nii.gz_brain_pve_0.nii.gz -V)
echo "$subj "CSF" $result1" >> $outDir/CSF_volume.txt

echo "extract volume for GM"
result3=$(fslstats $dataDir/"$subj".nii.gz_brain_pve_1.nii.gz -V)
echo "$subj "GM" $result3" >> $outDir/GM_volume.txt

echo "extract volume for WM"
result2=$(fslstats $dataDir/"$subj".nii.gz_brain_pve_2.nii.gz -V)
echo "$subj "WM" $result2" >> $outDir/WM_volume.txt
