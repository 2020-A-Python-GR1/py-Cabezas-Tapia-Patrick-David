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

class Puzzle:
    __imagen = misc.face()
    original = None
    imagen_actual = None
    piezas = None
    division_eje_x = 4
    division_eje_y = 4
    auxiliar = None
    error = ""

    
    def __init__(self):
        self.__imagen = misc.face()
        y1, y2, y3, y4 = np.vsplit(self.__imagen, self.division_eje_y)
        self.original = np.array([np.hsplit(y1, self.division_eje_x), np.hsplit(y2, self.division_eje_x), np.hsplit(y3, self.division_eje_x), np.hsplit(y4, self.division_eje_x)])
        self.piezas = self.original.copy()
        self.imagen_actual = np.zeros_like(self.original)
        self.crear_juego()
        self.armar_rompecabezas()
    
    
    def crear_juego(self):
        numero_de_piezas = self.division_eje_x * self.division_eje_y
        posiciones_iniciales = random.sample(range(numero_de_piezas), numero_de_piezas)
        contador = 0
        for posicion in posiciones_iniciales:
            self.imagen_actual[int(contador/self.division_eje_x), contador%self.division_eje_x] = self.piezas[int(posicion/self.division_eje_x), posicion%self.division_eje_x,:,:,:]
            contador = contador + 1
    
    
    def imprimir_rompecabezas(self):
        juego = np.vstack([np.hstack(self.imagen_actual[0,:,:,:,:]), np.hstack(self.imagen_actual[1,:,:,:,:]), np.hstack(self.imagen_actual[2,:,:,:,:]), np.hstack(self.imagen_actual[3,:,:,:,:])]) 
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 15))                 
        axes[0].imshow(juego)
        axes[1].imshow(self.__imagen)
        fig.tight_layout()
    
    
    # def intercambiar(self, inicial, final):
    #     auxiliar = np.copy(self.imagen_actual[int(inicial/self.division_eje_x), inicial%self.division_eje_x])
    #     self.imagen_actual[int(inicial/self.division_eje_x), inicial%self.division_eje_x] = self.imagen_actual[int(final/self.division_eje_x), final%self.division_eje_x]                  
    #     self.imagen_actual[int(final/self.division_eje_x), final%self.division_eje_x] = np.copy(auxiliar)
