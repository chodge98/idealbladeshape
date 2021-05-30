# Colin Hodge
# ME 236 - Renewable Energy Harvesting
# Final Project
# Ideal turbine blade shape
#5/15/2021


# Importing requried packages
import matplotlib.pyplot as plt
import math
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

# Defining constants
# Number of blades
N = 3

# Length of blades (m)
R = 10

# List of radial lengths (m)
r = np.linspace(1, 30, num = 100)

# Tip Speed ratio
lambda_opt = (4 * math.pi) / (N)

# Angle of attack/ Lift coefficient (assumed)
alpha = 12
cl = 1.5

# lambda_r list to append to
lambda_r = []

# Angle of relative wind list to append to
phi = []

# Chord length list to append to
chord_length = []

# Blade angle list to append to
blade_angle = []

# Cartesian points
cartx = []
carty = []

# Max/Min cartesian lists to append to (will be graphed)
x_min = []
x_max = []
y_min = []
y_max = []


# For loop to assign values for lambda_r
for i in r:
    tipspeed = lambda_opt * (i/R)
    lambda_r.append(tipspeed)


# For loop to assign values for phi
for i in lambda_r:
    rel_wind = math.atan(2/(3 * i))
    phi.append(rel_wind)

# For loop to assign values for chord_length
for i in range(0,len(r)):
    c = (8 * math.pi * r[i] * (math.sin(phi[i])) / ( 3 * N * cl * lambda_r[i]))
    chord_length.append(c)

# For loop to assign values for blade angle
for i in phi:
    a = (alpha * (math.pi / 180)) + i
    blade_angle.append(a)

# Converting values from polar to cartesian
for i in range(0,len(r)):
    x = (chord_length[i] * (math.cos(blade_angle[i])))
    y = (chord_length[i] * (math.sin(blade_angle[i])))
    cartx.append(x)
    carty.append(y)


# Centering values 
for i in range(0,len(r)):
    x_small = (-1) * cartx[i] / 2
    x_large = cartx[i] / 2
    y_small = (-1) * carty[i] / 2
    y_large = carty[i] / 2

# Assigning to lists to be graphed 
    x_min.append(x_small)
    x_max.append(x_large)
    y_min.append(y_small)
    y_max.append(y_large)


# Assigning variables to plot
# x values
i1 = x_min
i2 = x_max
# y values
j1 = y_min
j2 = y_max
# z values 
k1 = r
k2 = r

# Plotting ideal blade shape
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.plot(i1, j1, k1, color = 'red', linewidth= 5) 
ax.plot(i2, j2, k2, color = 'red', linewidth= 5)

# Connecting lines 
for i in range(len(i1)):
    ax.plot([i1[i], i2[i]], [j1[i], j2[i]], [k1[i], k2[i]], color = 'blue')

# Label and showing plot
ax.set_zlabel('Radial Direction (m)')
plt.show()












