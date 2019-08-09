set -x
subj=$1

mkdir -p /data/analysis_young/"$subj"_derivative/
bet /data/young/$subj /data/analysis_young/"$subj"_derivative/"$subj"_brain
