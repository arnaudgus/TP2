import numpy as np
import matplotlib.pyplot as plt
import math

"""
same with RK2 method
"""

# Params :
N=10000
dt=0.006
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
    xt=x[i]+y[i]*dt/2
    yt=y[i]-(A*y[i]+R*x[i])*dt/2

    dx = yt
    dy = -(A*yt+R*xt)

    x[i+1]=x[i] + dx*dt
    y[i+1]=y[i] + dy*dt

# plot
plt.figure()
plt.plot(t,x, color='r', linestyle="--")
plt.plot( xlabel = 't', ylabel = "x")
plt.show()