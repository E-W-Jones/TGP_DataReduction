# Perform image reduction, subtracting bias, dividing by flat field,
# and normalising to an exposure time of 1s
# Created for Cepheids1 Telescope Group Project
import numpy as np
from astropy.io import fits
import os
# Dont want it to print divide by 0 warnings
import warnings
import argparse

description = "Reduce the images in image_folder, saving them to reduced_folder."
parser = argparse.ArgumentParser(description=description)

parser.add_argument("image_folder",
                    help="The folder containing the images to be reduced.")

parser.add_argument("reduced_folder",
                    help="The folder where reduced images are saved to.")

parser.add_argument("-b", "--bias",
                    help="The master bias frame file.")

parser.add_argument("-f", "--flats",
                    help="The master flat field file.")

args = parser.parse_args()

BIAS_FNAME = args.bias if args.bias else "MasterBias.fits"
FLAT_FIELD_FNAME = args.flats if args.flats else "MasterFlat.fits"
BIAS = fits.getdata(BIAS_FNAME)
FLAT_FIELD = fits.getdata(FLAT_FIELD_FNAME)
IMAGE_FOLDER = args.image_folder
REDUCED_FOLDER = args.reduced_folder


# Iterate through every file, reducing and saving each image
image_fnames = [name for name in os.listdir(IMAGE_FOLDER)]
reduced_fnames = [os.path.join(REDUCED_FOLDER, f) for f in os.listdir(IMAGE_FOLDER)]

# Switch off divide by 0 warnings
warnings.filterwarnings("ignore", category=RuntimeWarning)

counter = {}

for image_name in image_fnames:
    image, header = fits.getdata(os.path.join(IMAGE_FOLDER, image_name), header=True)
    exposure_time = header['EXPOSURE']
    object = header['OBJECT']

    if object in counter:
        counter[object] += 1
    else:
        counter[object] = 0

    reduced_image = (image - BIAS) / FLAT_FIELD
    reduced_image /= exposure_time

    reduced_name = os.path.join(REDUCED_FOLDER, image_name)
    # reduced_name = os.path.join(REDUCED_FOLDER, f"{object}_reduced_{counter[object]}.fits")
    fits.writeto(reduced_name, reduced_image, header)
    print(f"{image_name} reduced to {reduced_name}")
