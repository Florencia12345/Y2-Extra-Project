from astropy.io import fits
from astropy.modeling import models, fitting 
import numpy as np 
import matplotlib.pyplot as plt 

path = '/Users/vivian/Desktop/Undergrad Study/Y2 Physics/Extra Project/DATA/subBack_Level3_ch1-long_s3d.fits'
hdul = fits.open(path)
hdul.info()

data = hdul[1].data
print(data)
print(len(data))
flux = data[1399,38]
print("flux is:", flux)  
print(len(flux))
# print(flux)

hdr = fits.getheader(path) # gets the header of the file
print(hdr)