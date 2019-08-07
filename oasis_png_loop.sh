

# create scan list file
rm scan_list.txt
rm subj_list.txt
cd ..
cd OASIS3_T1
ls | sed 's/_MR*/ /' | awk '{print $1}' | uniq >> subj_list.txt

# first loop: extract directory of first T1w image for each unique subject
for subj in $(cat 'subj_list.txt') ; do

echo "running script on $subj"


a=`ls "$subj"_MR_d*/* | awk 'NR==1{print $1}'`
a=`echo "${a::-1}"`
b=`ls $a | awk 'NR==2{print $1}'`
echo "$a"/"$b">> scan_list.txt

done

# second loop: for each first unique T1w, run pngify script
for scan in $(cat 'scan_list.txt') ; do

a=$scan
outputFolder=`echo $a | sed 's/_ses*/ /' | awk '{print $1}' | sed 's/sub-//'`
print $outputFolder

outDir=/home/ubuntu/data/oasis_pngimages/$outputFolder
mkdir -p $outDir

# run  script with input individual T1w image and output to
python convert_nii_to_png.py /home/ubuntu/OASIS3_T1/$scan $outDir

done
