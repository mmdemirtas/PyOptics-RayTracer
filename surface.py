import numpy as np

## düzlem yüzeyi oluşturduk. Bu sonsuz uzunlukta düz bir yüzeyi temsil ediyor.
class Planesurface:
    def __init__(self,y=0): 
        ##dışarıdan bir y değeri al. hiçbir y değeri gelmezse y yi sıfır kabul et
        
        self.y = y
        ## y'yi fonksiyon içinde kullanabilmeyi sağlar.

    def intersect(self,ray):
        ##kesişim noktasını bulmayı sağlar.

        origin_y = ray.position[1]
        direction_y = ray.direction[1]
        ## direction[0] x değeri direction[1] y değeri dir.

        if direction_y == 0:
            return None

        t = (self.y - origin_y)/direction_y
        ## y(t)=y0​+tdy​ burada t'yi yanlız bırak ve t'yi bul.

        hit_point = ray.position + t* ray.direction
        ## kesişim yerini bulur.

        return hit_point
class MirrorSurface(Planesurface):
    def reflect(self,ray):
        hit = self.intersect(ray)

        if hit is None:
            return None
    
        normal = np.array([0.0 , 1.0])
        ## Aynanın normali

        direction = ray.direction
        direction = direction/ np.linalg.norm(direction)
        
        reflected = direction - 2*np.dot(direction,normal) * normal
        ## np.dot dot producct yapar yani D.N direction ve normali çarpar. Çıkan sonuç normal vektörüyle çarpılır. R = D-2(D.N)N

        return hit, reflected
    
