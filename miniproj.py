import numpy as np
import matplotlib.pyplot as plt

# Step function examples (your code)
x = [0, 30, 30, 60, 60, 90, 90, 120]
y = [0, 0, 1, 1, 2, 2, 3, 3]

x2 = [0, 30, 30, 60, 60, 90, 90, 120]
y2 = [0, 0, 1, 1, 2, 2, 2, 2]

x3 = [0, 30, 30, 60, 60, 90, 90, 120]
y3 = [0, 0, 0, 0, 0, 0, 0, 0]

# SDE simulation settings
T = 120  # total time in minutes
dt = 1   # time step in minutes
N = int(T / dt)  # number of steps
time = np.linspace(0, T, N+1)

lambda_rate = 0.03  # touchdowns per minute (0.03 * 120 ≈ 3.6)
sigma = 0.2         # randomness factor

# Simulate a few SDE trajectories
np.random.seed(0)  # for reproducibility
num_paths = 10
trajectories = []

for _ in range(num_paths):
    X = np.zeros(N+1)
    for i in range(N):
        dW = np.random.normal(0, np.sqrt(dt))
        X[i+1] = X[i] + lambda_rate * dt + sigma * dW
    trajectories.append(X)

# Plot everything
plt.figure(figsize=(10, 5))

# Step function examples
plt.plot(x, y, drawstyle='steps-post', label='Possible Path 1 (Step)', color='blue', linewidth=2)
plt.plot(x2, y2, drawstyle='steps-post', label='Possible Path 2 (Step)', color='green', linewidth=2)
plt.plot(x3, y3, drawstyle='steps-post', label='Possible Path 2 (Step)', color='red', linewidth=2)


# Stochastic trajectories
for i, X in enumerate(trajectories):
    plt.plot(time, X, alpha=0.7, linestyle='--', label=f'Stochastic Path {i+1}')

plt.xlabel('time (min)')
plt.ylabel('touchdowns')
plt.tight_layout()
plt.show()
