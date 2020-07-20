import numpy as np
from scipy import ndimage
from scipy import misc
import random
import matplotlib.pyplot as plt


class Puzzle:

    def __init__(self):
        self.dimenciones = 2
        self.imagen = misc.face()
        self.y=np.vsplit(self.imagen, self.dimenciones)        
        self.v=[]   
        self.posicion_valor=[self.dimenciones-1,self.dimenciones-1]
        for i in range(self.dimenciones):
            self.v.append(np.hsplit(self.y[i], self.dimenciones))        
        self.imagen_original = np.array(self.v)
        self.imagen_piezas = self.imagen_original.copy()
        self.imagen_piezas[self.dimenciones-1,self.dimenciones-1,:,:,:]=np.zeros_like(self.imagen_piezas[self.dimenciones-1,self.dimenciones-1,:,:,:])
        self.imagen_original = np.copy(self.imagen_piezas)
        self.imagen_auxiliar = np.zeros_like(self.imagen_original)
        self.armar_puzzle()
        self.imprimir_puzzle()
        self.ejecutar_puzzle()       
    
    def armar_puzzle(self):
        numero_piezas = pow(self.dimenciones,2)
        posiciones_random = random.sample(range(numero_piezas), numero_piezas)
        contador = 0
        for posicion in posiciones_random:
            self.imagen_auxiliar[int(contador/self.dimenciones),contador%self.dimenciones] = self.imagen_piezas[int(posicion/self.dimenciones),posicion%self.dimenciones,:,:,:]
            if(int(posicion/self.dimenciones)==self.dimenciones-1 and posicion%self.dimenciones==self.dimenciones-1):
                self.posicion_valor=[int(contador/self.dimenciones),contador%self.dimenciones]
            contador = contador + 1 

    def imprimir_puzzle(self):
        auxiliar = []
        for i in range(self.dimenciones):
            auxiliar.append(np.hstack(self.imagen_auxiliar[i,:,:,:,:]))
        juego = np.vstack(auxiliar)
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 15))
        axes[0].imshow(self.imagen)            
        axes[1].imshow(juego)        
        fig.tight_layout()    

    def ejecutar_puzzle(self):        
        while(1):
            plt.pause(1)
            self.comprobar_completado()
            valor = input("←(a)  ↑(w)  →(d)   ↓(s)  q (salir)")
            if(valor == "a"):
                if(self.posicion_valor[1] != 0):
                    auxiliar = np.copy(self.imagen_auxiliar[self.posicion_valor[0],self.posicion_valor[1]-1])
                    self.imagen_auxiliar[self.posicion_valor[0],self.posicion_valor[1]-1] = self.imagen_auxiliar[self.posicion_valor[0],self.posicion_valor[1]]
                    self.imagen_auxiliar[self.posicion_valor[0],self.posicion_valor[1]] = np.copy(auxiliar)
                    self.posicion_valor[1]=self.posicion_valor[1]-1
                else:
                    print("no puede realizar esete movimiento")
            if(valor == "w"):
                if(self.posicion_valor[0] != 0):
                    auxiliar = np.copy(self.imagen_auxiliar[self.posicion_valor[0]-1,self.posicion_valor[1]])
                    self.imagen_auxiliar[self.posicion_valor[0]-1,self.posicion_valor[1]] = self.imagen_auxiliar[self.posicion_valor[0],self.posicion_valor[1]]
                    self.imagen_auxiliar[self.posicion_valor[0],self.posicion_valor[1]] = np.copy(auxiliar)
                    self.posicion_valor[0]=self.posicion_valor[0]-1
                else:
                    print("no puede realizar esete movimiento")
            if(valor == "s"):
                if(self.posicion_valor[0] != self.dimenciones-1):
                    auxiliar = np.copy(self.imagen_auxiliar[self.posicion_valor[0]+1,self.posicion_valor[1]])
                    self.imagen_auxiliar[self.posicion_valor[0]+1,self.posicion_valor[1]] = self.imagen_auxiliar[self.posicion_valor[0],self.posicion_valor[1]]
                    self.imagen_auxiliar[self.posicion_valor[0],self.posicion_valor[1]] = np.copy(auxiliar)
                    self.posicion_valor[0]=self.posicion_valor[0]+1
                else:
                    print("no puede realizar esete movimiento")
            if(valor == "d"):
                if(self.posicion_valor[0] != self.dimenciones-1):
                    auxiliar = np.copy(self.imagen_auxiliar[self.posicion_valor[0],self.posicion_valor[1]+1])
                    self.imagen_auxiliar[self.posicion_valor[0],self.posicion_valor[1]+1] = self.imagen_auxiliar[self.posicion_valor[0],self.posicion_valor[1]]
                    self.imagen_auxiliar[self.posicion_valor[0],self.posicion_valor[1]] = np.copy(auxiliar)   
                    self.posicion_valor[1]=self.posicion_valor[1]+1                    
                else:
                    print("no puede realizar esete movimiento")
            if(valor == "q"):
                break
            self.imprimir_puzzle()

    def comprobar_completado(self):
        if np.array_equal(self.imagen_auxiliar, self.imagen_original):
            input("Logro Finalizar")  
            exit()      

puzzle = Puzzle()