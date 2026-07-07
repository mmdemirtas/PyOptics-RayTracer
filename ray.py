import numpy as np

class Ray:
    def __init__(self,position,direction):

     self.position = np.array(position, dtype=float)
     ## konum bilgisi np de float veri dipine çevriliyor. self kullanınca bu artık tüm fonksiyonlarda erişime açık??

     direction = np.array(direction, dtype=float)
     ## yönü de float'a çevirdik

     self.direction = direction / np.linalg.norm(direction) 
     ## Burada yön vektörünü yön vektörünün uzunluğuna böldük. bu sayede elimizde sadece vektörün yönü bilgisi kaldı.

     self.history = [self.position.copy()] 
     ## copy() yazmasak history ile aynı belleği büyük paylaşırdı. self.history ile ilk pozisyonu kaydetmiş olduk.

    def propogate(self,distance):
       self.position = self.direction * distance
       ## eski konuma yön çarpı aldığımız mesafeyi ekleyip yeni konumumuzu buluyoruz.

       self.history.append(self.position.copy())
       ## Geçtiği yeni nokta history'e kaydedildi.

## Sonuç olarak: position(şuan bulunduğu nokta) direction(birim yön vektörü) history(geçtiği tüm noktalar)
