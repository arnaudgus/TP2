import numpy as np
import matplotlib.pyplot as plt
import math

# Params :
N=10000
dt=0.002
R=4*(math.pi)**2
A=0.1
x0=1
y0=0

# Vectors :
x = np.zeros(N)
y = np.zeros(N)
t = np.arange(start = 0, stop = N) * dt

# Init 
x[0]=x0
y[0]=y0

# Loop
for i in range(N-1):
    x[i+1]=x[i]+y[i]*dt
    y[i+1]=y[i]-(A*y[i]+R*x[i])*dt

# print(y)
# print(x)
# print(t)

# plot
plt.figure()
plt.plot(t,x)
plt.show()