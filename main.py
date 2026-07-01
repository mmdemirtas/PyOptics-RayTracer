from src.ray import Ray
from src.surface import PlaneSurface
import numpy as np
import matplotlib.pyplot as plt

ray = Ray([0, 2], [1, -0.5])
surface = PlaneSurface(z=0)

hit = surface.intersect(ray)

ray.propagate(5)

h = np.array(ray.history)

plt.plot(h[:,0], h[:,1])

if hit is not None:
    plt.scatter(hit[0], hit[1], color='red', s=80)

plt.axhline(0)
plt.axis("equal")
plt.grid()
plt.show()
