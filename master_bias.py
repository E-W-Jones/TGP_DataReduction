# Take an average bias frame from a folder of bias frames.
# Created for Cepheids1 Telescope Group Project
import numpy as np
from astropy.io import fits
import os
import argparse

description = ("Combine the frames in bias_folder to create a master bias. "
               "This is saved by default as 'MasterBias.fits'")
parser = argparse.ArgumentParser(description=description)

parser.add_argument("bias_folder",
                    help="The folder containing the images to be stacked.")

parser.add_argument("-s", "--save_to",
                    help="The file to save it to.")

parser.add_argument("-m", "--mean",
                    help="Whether or not to find the mean, or median (default)",
                    action="store_true")

args = parser.parse_args()

BIAS_FOLDER = args.bias_folder
USE_MEDIAN = not args.mean
OUTPUT_NAME = args.save_to if args.save_to else "MasterBias.fits"

# create a list of filenames to read from
bias_fnames = [os.path.join(BIAS_FOLDER, f) for f in os.listdir(BIAS_FOLDER)]

# Create a stack of bias frames
bias_frames = np.array([fits.getdata(f) for f in bias_fnames])

# Find the average (not sure which one we want to use)
median_bias = np.median(bias_frames, axis=0)
mean_bias = np.mean(bias_frames, axis=0)

# Pick the one you want to use
master_bias = median_bias if USE_MEDIAN else mean_bias

fits.writeto(OUTPUT_NAME, master_bias)
print(f"Created master bias from folder: {BIAS_FOLDER}")
