set -x
subj=$1

mkdir -p /home/ubuntu/data/reconstructed_nifti/analysis_young/"$subj"_derivative/
fast /home/ubuntu/data/reconstructed_nifti/analysis_young/"$subj"_derivative/"$subj"_brain
