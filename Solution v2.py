import pandas as pd
import numpy as np
from math import *
import matplotlib.pyplot as plt


a=[]
for x in range(100):
	a.append(2*pi*x/100)


csv_data = pd.read_csv("CometData.csv")
data_array = csv_data.to_numpy()


time_data = data_array[:,0]
distance_from_earth_array = data_array[:,1]
angle_bw_sun_and_comet_array = data_array[:,2]


r = distance_from_earth_array
θ = -angle_bw_sun_and_comet_array

    
polar_distance = np.sqrt(1 + r**2 - 2*r*np.cos(θ))
alpha_array = np.arccos((1 - r*np.cos(θ))/polar_distance)
polar_angle = []

for x in range(100):
    theta = θ[x]
    α = alpha_array[x]
    T = time_data[x]
    if (theta>=0):
        polar_angle.append(α+2*pi*T)
        
    if (theta<0):
        polar_angle.append(-α+2*pi*T)


plt.polar(polar_angle,polar_distance)
plt.show()









