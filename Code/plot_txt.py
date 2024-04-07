import numpy as np
import matplotlib.pyplot as plt 

path = "/Users/vivian/Desktop/Undergrad Study/Y2 Physics/Extra Project/DATA/NGC 3256_Nuc1_SF1_1D.txt"
data = np.loadtxt(path, delimiter=" ")


wavelength = data[:, 0]
spectrum = data[:, 1]
error = data[:, 2]

plt.step(wavelength, spectrum, where='mid', color='k')
plt.xlabel(r"Wavelength ($\AA$)", fontsize=18)
plt.ylabel(r"Flux (Jy)$", fontsize=18)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.yscale('log', base = 10)
plt.show()