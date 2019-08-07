

# create scan list file
rm scan_list.txt
rm subj_list.txt
ls | sed 's/_MR*/ /' | awk '{print $1}' | uniq >> subj_list.txt

# first loop: extract directory of first T1w image for each unique subject
for subj in $(cat 'subj_list.txt') ; do

echo "running script on $subj"
ls ${subj}_MR_d*/* | awk 'NR==3{print $1}' >> scan_list.txt

done

# second loop: for each first unique T1w, run pngify script
for scan in $(cat 'scan_list.txt') ; do

a = ${scan}_MR_d*/* | awk 'NR==3{print $1}' | sed 's/_ses*/ /' | awk '{print $1}' | sed 's/sub-//'
outDir=/home/ubuntu/data/oasis_pngimages/$a
mkdir -p $outDir

# run  script with input individual T1w image and output to
sh python convert_nii_to_png.py -i /home/ubuntu/OASIS3_T1/$scan -o $outDir

done
