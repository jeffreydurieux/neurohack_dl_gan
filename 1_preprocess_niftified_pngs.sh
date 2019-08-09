set -x
subj=$1

mkdir -p /data/"$subj"_derivative/
bet /data/$subj /data/"$subj"_derivative/"$subj"_brain
