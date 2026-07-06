import numpy as np

class PlaneSurface:
    def __init__(self, z=0):
        self.z = z

    def intersect(self, ray):
        origin_z = ray.position[1]
        direction_z = ray.direction[1]

        if direction_z == 0:
            return None

        t = (self.z - origin_z) / direction_z

        if t < 0:
            return None

        hit_point = ray.position + t * ray.direction
        return hit_point


class MirrorSurface(PlaneSurface):

    def reflect(self, ray):

        hit = self.intersect(ray)

        if hit is None:
            return None

        # Aynanın normali (yukarı bakıyor)
        normal = np.array([0.0, 1.0])

        direction = ray.direction
        direction = direction / np.linalg.norm(direction)

        reflected = direction - 2 * np.dot(direction, normal) * normal

        return hit, reflected
