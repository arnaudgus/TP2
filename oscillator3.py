import numpy as np
import matplotlib.pyplot as plt
import math

"""
Implicit Euler method
"""
# Params :
N=5000
dt=0.006
R=4*(math.pi)**2
A=0.1
x0=1
y0=0

# Vectors :
X = np.zeros((2,N))
t = np.arange(start = 0, stop = N) * dt

# Init 
print(X)
print(X[:,0])
xO = np.array([x0,y0])
print(X.shape)
print(xO.shape)

X[:,0].fill(1)

# Loop
M = np.array([[1, -dt], [R*dt, 1+A*dt]])
iM = np.linalg.inv(M)
print(iM)
for i in range(N-1):
    b = X[:,0]
    X[:,i+1] = np.multiply(iM, b)

# plot
plt.figure()
plt.plot(t,X, color='r')
plt.show()