import numpy as np

class PlaneSurface:
    def __init__(self, z=0):
        self.z = z

    def intersect(self, ray):
        # ray: origin + t * direction

        origin_z = ray.position[1]
        direction_z = ray.direction[1]

        if direction_z == 0:
            return None  # paralel

        t = (self.z - origin_z) / direction_z

        if t < 0:
            return None  # arkada kalıyor

        hit_point = ray.position + t * ray.direction
        return hit_point
