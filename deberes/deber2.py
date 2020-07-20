import numpy as np
import matplotlib.pyplot as plt
from scipy import ndimage
from scipy import misc

print("todo bien ")

dimencion=3
x = int(1024/dimencion)
y = int(768/dimencion)
mapache=misc.face()
print(mapache.shape)
mapa=np.array(mapache)
#A=np.arange(8).reshape(2,4)
#juego = np.vstack([np.hstack(mapa[0,:,:,:,:]), np.hstack(mapa[1,:,:,:,:]), np.hstack(mapa[2,:,:,:,:]) ])
#(768, 1024, 3)
#print(mapa.reshape(-1,1024),3))
resultado = mapa[0:y,0:x,:]
print(resultado.shape)
#plt.imshow(resultado)

numero_de_piezas = self.division_eje_x * self.division_eje_y
    posiciones_iniciales = random.sample(range(9), 9)
    contador = 0
    for posicion in posiciones_iniciales:
        self.imagen_actual[int(contador/self.division_eje_x), contador%self.division_eje_x] = self.piezas[int(posicion/self.division_eje_x), posicion%self.division_eje_x,:,:,:]
        contador = contador + 1


fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 15))                 
axes[0].imshow(mapache)
axes[1].imshow(resultado)
fig.tight_layout()
plt.show()

