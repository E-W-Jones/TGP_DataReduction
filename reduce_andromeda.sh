#/bin/bash

[ -a ../ReducedData/Andromeda/2021-10-01/V ] && rm -r ../ReducedData/Andromeda/2021-10-01/V
mkdir -p ../ReducedData/Andromeda/2021-10-01/V


[ -a ../ReducedData/Andromeda/2021-10-01/B ] && rm -r ../ReducedData/Andromeda/2021-10-01/B
mkdir -p ../ReducedData/Andromeda/2021-10-01/B


[ -a ../ReducedData/Andromeda/2021-10-13/V ] && rm -r ../ReducedData/Andromeda/2021-10-13/V
mkdir -p ../ReducedData/Andromeda/2021-10-13/V


[ -a ../ReducedData/Andromeda/2021-10-13/B ] && rm -r ../ReducedData/Andromeda/2021-10-13/B
mkdir -p ../ReducedData/Andromeda/2021-10-13/B

# Reduce the exposures taken in the V band on the 1st of october
python3 reduce.py -f MasterFlatV.fits ../AndromedaObservations/V ../ReducedData/Andromeda/2021-10-01/V

# Reduce exposures taken in B band on 1st
python3 reduce.py -f MasterFlatB.fits ../AndromedaObservations/B ../ReducedData/Andromeda/2021-10-01/B

# Reduce exposures taken on 13th in B and V
python3 reduce.py -f MasterFlatV.fits ../AndromedaObservations/V_std ../ReducedData/Andromeda/2021-10-13/V

python3 reduce.py -f MasterFlatB.fits ../AndromedaObservations/B_std ../ReducedData/Andromeda/2021-10-13/B
