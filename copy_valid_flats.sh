#!/bin/bash

BAND=$1
PATHTOFLATS=/storage/teaching/2021-22/tgp/PIRATE_data/Calibrations
PATHTOSAVE=/storage/teaching/2021-22/tgp/Cepheids1/DataReduction/Flats$BAND

# If no flats folder, create it
[ ! -d "$PATHTOSAVE" ] && mkdir "$PATHTOSAVE"

# Flats taken in the evening (date_19) are 2x2 binning
# Flats taken in the morning (so timestamped date_05_ or _06) are 1x1 binning
# File looks like:
# PIRATE_######_flats_(FILTER)_##_YYYY_MM_DD_HH_MM_SS.fits
# So want to copy something that goes:
# *flats_V_??_2021_10_??_0?_??_??.fits
# This says any flat in the V band taken in october in the AM (time reads 01, 02, ...)

echo "Copy the $BAND band flats from October, that are taken in the morning"
# Copies any dates that start with a 0 but not followed by a 1 (02, 03, ..., 09), or start w/ a 1 but arent followed by 7, 8, 9
cp --recursive {$PATHTOFLATS/*/*"flats_$BAND"_??_2021_10_0[!1]_0?_??_??.fits,$PATHTOFLATS/*/*"flats_$BAND"_??_2021_10_1[!7-9]_0?_??_??.fits} $PATHTOSAVE
