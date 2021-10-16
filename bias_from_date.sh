#!/usr/bin/env bash

DATE=$1
PATHTOBIAS="/storage/teaching/2021-22/tgp/PIRATE_data/Calibrations/$DATE"
SAVETO="/storage/teaching/2021-22/tgp/Cepheids1/DataReduction/MasterBias.fits"
TEMPFILE="/scratch/$USER/"

echo "Creating a temporary file on the scratch disk"
mkdir -p $TEMPFILE

echo "Copying 1x1 Binned Bias frames from $DATE"
cp $PATHTOBIAS/*Bias11* $TEMPFILE

echo "Running python master_bias script"
python3 master_bias.py $TEMPFILE --save_to $SAVETO

echo "Delete the temporary file from scratch disk"
rm -r $TEMPFILE

echo "Bash Script Completed"
