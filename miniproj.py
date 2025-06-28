import numpy as np
import matplotlib.pyplot as plt

# step funs
x = [0, 30, 30, 60, 60, 90, 90, 120]
y = [0, 0, 1, 1, 2, 2, 3, 3]

x2 = [0, 30, 30, 60, 60, 90, 90, 120]
y2 = [0, 0, 1, 1, 2, 2, 2, 2]

x3 = [0, 30, 30, 60, 60, 90, 90, 120]
y3 = [0, 0, 0, 0, 0, 0, 0, 0]

# SDE simulation vars
time = 120  # time (min)
dt = 1   # time step (min)
N = int(time / dt)  # number of steps
time = np.linspace(0, time, N+1)

lambda_rate = 0.03  # td/m (example)
sigma = 0.2         

# trajectory
np.random.seed(0)
num_paths = 10

# make traj
trajectories = []
for _ in range(num_paths):
    X = np.zeros(N+1)
    for i in range(N):
        dW = np.random.normal(0, np.sqrt(dt))
        X[i+1] = X[i] + lambda_rate * dt + sigma * dW
    trajectories.append(X)

# plot
plt.figure(figsize=(10, 5))
plt.plot(x, y, drawstyle='steps-post', color='blue', linewidth=2)
plt.plot(x2, y2, drawstyle='steps-post', color='green', linewidth=2)
plt.plot(x3, y3, drawstyle='steps-post', color='red', linewidth=2)

# SDEs
for i, X in enumerate(trajectories):
    plt.plot(time, X, alpha=0.7, linestyle='--')

plt.xlabel('time (min)')
plt.ylabel('touchdowns')
plt.tight_layout()
plt.show()
