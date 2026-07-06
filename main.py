from src.ray import Ray
from src.surface import MirrorSurface
import matplotlib.pyplot as plt
import numpy as np

ray = Ray([0,2],[1,-0.5])

mirror = MirrorSurface(z=0)

result = mirror.reflect(ray)

if result is not None:

    hit, new_dir = result

    ray.propagate(np.linalg.norm(hit-ray.position))

    reflected_ray = Ray(hit, new_dir)
    reflected_ray.propagate(5)

    h1 = np.array(ray.history)
    h2 = np.array(reflected_ray.history)

    plt.plot(h1[:,0],h1[:,1],label="Incident Ray")
    plt.plot(h2[:,0],h2[:,1],label="Reflected Ray")

    plt.scatter(hit[0],hit[1],color="red",s=70)

plt.axhline(0)

plt.axis("equal")
plt.grid()
plt.legend()
plt.show()
