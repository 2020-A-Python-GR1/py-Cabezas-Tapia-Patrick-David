from IPython.display import clear_output
import numpy as np
from time import sleep
import math
from scipy import ndimage
from scipy import misc
import random
import matplotlib.pyplot as plt


class Puzzle:
    error = ""

    def __init__(self):
        self.dimenciones = 4
        self.imagen = misc.face()
        self.y=np.vsplit(self.imagen, self.dimenciones)        
        self.v=[]        
        for i in range(self.dimenciones):
            self.v.append(np.hsplit(self.y[i], self.dimenciones))        
        self.original = np.array(self.v)
        self.piezas = self.original.copy()
        self.imagen_actual = np.zeros_like(self.original)
        self.crear_juego()
        self.imprimir_rompecabezas()
        plt.pause(10)     
        #self.armar_rompecabezas()    
    
    def crear_juego(self):
        numero_de_piezas = pow(self.dimenciones,2)
        posiciones_iniciales = random.sample(range(numero_de_piezas), numero_de_piezas)
        #print(np.array(self.piezas).shape)
        contador = 0
        for posicion in posiciones_iniciales:
            self.imagen_actual[int(contador/self.dimenciones),contador%self.dimenciones] = self.piezas[int(posicion/self.dimenciones),posicion%self.dimenciones,:,:,:]
            contador = contador + 1    
    
    def imprimir_rompecabezas(self):
        v_aux = []
        for i in range(self.dimenciones):
            v_aux.append(np.hstack(self.imagen_actual[i,:,:,:,:]))
        juego = np.vstack(v_aux)
        fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(15, 15))                 
        axes[1].imshow(juego)
        axes[0].imshow(self.imagen)
        fig.tight_layout()    
    
    def intercambiar(self, inicial, final):
        auxiliar = np.copy(self.imagen_actual[int(inicial/self.dimenciones), inicial%self.dimenciones])
        self.imagen_actual[int(inicial/self.dimenciones), inicial%self.dimenciones] = self.imagen_actual[int(final/self.dimenciones), final%self.dimenciones]                  
        self.imagen_actual[int(final/self.dimenciones), final%self.dimenciones] = np.copy(auxiliar)
        
        
    def armar_rompecabezas(self):
        while True:
            clear_output()
            if self.error == "":
                pass
            else:
                print(self.error)
            self.error = ""
            self.imprimir_rompecabezas()
            plt.pause(1)
            
            try:
                inicial = int(input("Ingrese la posicion de la pieza que desea mover: "))
                final = int(input("Ingrese la posicion a la que desea mover la pieza: "))
            except Exception:
                self.error = "hHa ingresado un numero incorrecto"
                continue
            
            if inicial < 0 or inicial > 15 or final < 0 or final > 15:
                self.error = "Debe ingresar como posicion un numero entre 0 y 15"
            
            else:
                self.intercambiar(inicial, final)
            
            if np.array_equal(self.imagen_actual, self.original):
                break
                
        clear_output()
        print("Completado con exito")
        self.imprimir_rompecabezas()

puzzle = Puzzle()