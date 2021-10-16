#!/bin/bash
echo "Reducing the Standard Stars"

[ -a ../ReducedData/Standards ] && rm -r ../ReducedData/Standards

mkdir ../ReducedData/Standards

echo "In the V band"
python3 reduce.py -f MasterFlatV.fits ../StandardStars/V ../ReducedData/Standards

echo "In the B band"
python3 reduce.py -f MasterFlatB.fits ../StandardStars/B ../ReducedData/Standards
