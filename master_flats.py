# Read all flat frames, set all of them to have the same number of counts on average
# Created for Cepheids1 Telescope Group Project
import numpy as np
from astropy.io import fits
import os
import argparse

description = ("Combine the frames in flats_folder to create a master flat. "
               "This is saved by default as 'MasterFlat.fits'")
parser = argparse.ArgumentParser(description=description)

parser.add_argument("flats_folder",
                    help="The folder containing the images to be stacked.")

parser.add_argument("bias",
                    help="The master bias frame.")

parser.add_argument("-s", "--save_to",
                    help="The file to save it to.")

args = parser.parse_args()

FLATS_FOLDER = args.flats_folder
BIAS = fits.getdata(args.bias)
OUTPUT_NAME = args.save_to if args.save_to else "MasterFlat.fits"


# Take median pixel value, and normalise this master flat

# read in the data from the fits files
flats_fnames = [os.path.join(FLATS_FOLDER, f) for f in os.listdir(FLATS_FOLDER)]
flats_data = [fits.getdata(f, header=True) for f in flats_fnames]

# Check the binning is correct, we only want 1x1
headers = [f[1] for f in flats_data]
binning = np.r_[[(h['XBINNING'], h['YBINNING']) for h in headers]]
if not np.all(binning == 1):
    raise ValueError("At least one of flat frames has the wrong binning")

# Subtract bias from flat field before performing analysis
flats = np.c_[[data[0] - BIAS for data in flats_data]]

mean_counts = np.mean(flats, axis=(1, 2))
mean_of_mean = np.mean(mean_counts)

# Scale so each flat has the same mean counts
flats *= mean_of_mean / mean_counts[:, np.newaxis, np.newaxis]

# Find the median, normalise, and make this the master flat
master_flat = np.median(flats, axis=0)
master_flat /= np.mean(master_flat)

fits.writeto(OUTPUT_NAME, master_flat)
print(f"Created master flat field from folder: {FLATS_FOLDER}")
