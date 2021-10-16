#!/bin/bash
DATE=$1
TGPPATH=/storage/teaching/2021-22/tgp/Cepheids1
RAW=$TGPPATH/CepheidObservations/$DATE
RED=$TGPPATH/ReducedData/$DATE

if [ -d $RED ]
then
    rm -r $RED
fi

mkdir $RED

# Don't need this bit anymore, since manually created folder to delete blurry exposures
#mkdir -p /scratch/$USER
# Copy all objects that either: don't begin with A (andromeda); have a T in the second place (STD stars)
#cp $RAW/*Ceph1_[!A][!T]* /scratch/$USER

python3 reduce.py $RAW $RED -f MasterFlatV.fits

# Don't need this
#rm -r /scratch/$USER
