from ray import Ray
import matplotlib.pyplot as plt
import numpy as np

ray = Ray(position=[0,2], direction=[1,0])

for i in range(10):
    ray.propagate(1)

history = np.array(ray.history)

plt.figure(figsize=(8,4))
plt.plot(history[:,0], history[:,1], linewidth=2)
plt.scatter(history[:,0], history[:,1])
plt.grid(True)
plt.axis("equal")
plt.xlabel("x (mm)")
plt.ylabel("y (mm)")
plt.title("Single Ray Propagation")
plt.show()
