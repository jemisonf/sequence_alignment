#/bin/bash

for i in 500 1000 2000 4000 5000
do
    echo "trial no, time" > trial_$i.csv
    python36 ./create_input.py $i
    time=$( { /usr/bin/time -f %e python36 ./sequence_aligner.py ; } 2>&1 )
    echo "$i,$time"
    echo "$i,$time" >> "trial_$i.csv"
done
