import pandas as pd
import numpy as np
import math as mt
import matplotlib.pyplot as plt


csv_data = pd.read_csv("CometData.csv")
data_array = csv_data.to_numpy()


time_data = data_array[:,0]
radius_data = data_array[:,1]
angle_data = data_array[:,2]



polar_radius = []
polar_angle = []


for x in range(100):
    if (angle_data[x] >= 0):
        theta = angle_data[x]
        theta_earth = time_data[x]*2*mt.pi
        R = radius_data [x]
        theta_polar = theta_earth + mt.acos((1-R*mt.cos(theta))/mt.sqrt(1+R**2-2*R*mt.cos(theta)))
        r_polar = mt.sqrt(1+R**2-2*R*mt.cos(theta))

        polar_radius.append(r_polar)
        polar_angle.append(theta_polar)

    else:
        theta = -angle_data[x]
        theta_earth = time_data[x]*2*mt.pi
        R = radius_data [x]
        theta_polar = theta_earth - mt.acos((1-R*mt.cos(theta))/mt.sqrt(1+R**2-2*R*mt.cos(theta)))
        r_polar = mt.sqrt(1+R**2-2*R*mt.cos(theta))

        polar_radius.append(r_polar)
        polar_angle.append(theta_polar)



plt.polar(polar_angle , polar_radius)
plt.show()


plt.axes(projection='polar')
c = plt.scatter(polar_angle,polar_radius)
plt.show()


y_data = mt.pi*2*time_data*np.sin(angle_data) + radius_data*np.sin(angle_data + 2*mt.pi*time_data)
x_data = mt.pi*2*time_data*np.cos(angle_data) + radius_data*np.cos(angle_data + 2*mt.pi*time_data)


plt.plot(x_data,y_data)
plt.show()


Y_DATA=[]
X_DATA=[]

for x in range(100):
    wt = 2*mt.pi*time_data[x]
    R = radius_data [x]
    
    if (angle_data[x] >= 0):
        theta = mt.pi-angle_data[x]
        
        X = mt.cos(wt) + R*mt.cos(theta+wt)
        Y = mt.sin(wt) + R*mt.sin(theta+wt)
        
        X_DATA.append(X)
        Y_DATA.append(Y)

    else:
        theta = -angle_data[x] - (mt.pi - wt)
        
        X = mt.cos(wt) + R*mt.cos(theta)
        Y = mt.sin(wt) + R*mt.sin(theta)
        
        X_DATA.append(X)
        Y_DATA.append(Y)
        
plt.plot(X_DATA,Y_DATA)
plt.show()
