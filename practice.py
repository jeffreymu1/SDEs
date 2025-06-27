import numpy as np
from matplotlib import pyplot as plt

t=np.linspace(0,10,101)
y=np.zeros([101])

y[0]=1

for i in range(1,101):
    y[i] = y[i-1]+0.1*(-y[i-1]+np.sin(t[i-1]))

plt.plot(t,y,'o')
plt.show()