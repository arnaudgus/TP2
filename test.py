from math import pi
from numpy import arange
import matplotlib.pyplot as plt

N = 5000
dt = 0.006
R = 4*pi**2
A = 0.1
x = [1]
y = [0]

t = arange(0, (N-1)*dt, dt)

for i in range(1, N-1):
    nx = x[-1] + y[-1]*dt
    ny = y[-1] - (A*y[-1] + R*x[-1])*dt
    x += [nx]
    y += [ny]

plt.figure()
plt.plot(t,x)
plt.show()