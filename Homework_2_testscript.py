'''Homework 2, Computational Photonics, SS 2020:  Beam propagation method.
'''

import numpy as np
from Homework_2_function_headers import waveguide, gauss, beamprop_CN
from matplotlib import pyplot as plt

# computational parameters
z_end   = 100       # propagation distance
lam     = 1         # wavelength
nd      = 1.455     # reference index
xa      = 50        # size of computational window
Nx      = 251       # number of transverse points
dx      = xa/(Nx-1) # transverse step size

# waveguide parameters
xb      = 2.0       # size of waveguide
n_cladding  = 1.45      # cladding index
n_core  = 1.46      # core refr. index

# source width
w       = 5.0       # Gaussian beam width

# propagation step size
dz = 0.5
output_step = np.round(1.0/dz)

# create index distribution
n, x = waveguide(xa, xb, Nx, n_cladding, n_core)

# create initial field
v_in, x = gauss(xa, Nx, w)
v_in = v_in/np.sqrt(np.sum(np.abs(v_in)**2)) # normalize power to unity
