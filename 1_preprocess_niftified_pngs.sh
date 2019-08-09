set -x
subj=$1

mkdir -p /home/ubuntu/data/reconstructed_nifti/analysis_young/"$subj"_derivative/
bet /home/ubuntu/data/reconstructed_nifti/young/$subj /home/ubuntu/data/reconstructed_nifti/analysis_young/"$subj"_derivative/"$subj"_brain
