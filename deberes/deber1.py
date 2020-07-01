class Marca_auto:
    nombre=None#stirng
    pais_origen=None#string
    fecha_creacion=None#date
    sucursal_local=None#boolean
    valor=None #int or float
    
    def __init__(self,nombre,pais_origen,fecha_creacion,sucursal_local,valor):        
        self.nombre=nombre
        self.pais_origen=pais_origen
        self.fecha_creacion=fecha_creacion
        self.sucursal_local=sucursal_local
        self.valor=valor
    
    def __str__(self):
        return f"Nombre: {self.nombre} Pais de Origen: {self.pais_origen} Fecha de creacion: {self.fecha_creacion} Sucursal Local: {self.sucursal_local} Valor: {self.valor}"

class Modelo_auto:
    nombre=None#string
    tipo=None#int
    precio_bace=None#float
    hibrido=None#bool
    marca=None #strig

    def __init__(self,nombre,tipo,precio_bace,hibrido,marca):
        self.nombre=nombre
        self.tipo=tipo
        self.precio_bace=precio_bace
        self.hibrido=hibrido
        self.marca=marca

    def __str__(self):
        return f"[modelo]Nombre: {self.nombre} tipo: {self.tipo} precio: {self.precio_bace}$ hibrido {self.hibrido} Marca: {self.marca}"

def agregarMarca():
    nombre=input("Ingresen el nombre de la marca: ")
    pais_origen=input("Ingresen el pais de origen de la marca: ")
    fecha_creacion=input("Ingresen la fecha de creacion de la marca(12-06-2020): ")
    sucursal_local=input("Ingresen True o False si existe sucurla en su pais: ")
    valor=input("Ingresen el valor de la empresa(100000): ")
    marcas.append(Marca_auto(nombre,pais_origen,fecha_creacion,sucursal_local,valor))


def eliminarMarca():
    nombre=input("Ingresen el nombre de la marca: ")
    estado=False
    for i in marcas:
        if(nombre== i.nombre):
            marcas.remove(i)
            eliminarModeloMarca(nombre)
            estado=True
            break
    if(not estado):
        print("No existe la Marca")

def eliminarModeloMarca(marca):
    opten=filter(lambda Modelo_auto: Modelo_auto.marca==marca,modelos)
    for i in opten:
        modelos.remove(i)

def mostrarMarcas():
    for i in marcas:
        print(i)

def actualizarMarcas():
    nombre=input("Ingresen el nombre de la marca: ")
    estado=False
    for i in marcas:
        if(nombre == i.nombre):
            marcas.remove(i)
            agregarMarca()
            estado=True
            break
    if(not estado):
        print("No existe el elemento")

def guardaMarcas():
    try:
        path = "/home/d/Documentos/programacion/practiva/marcas.txt"
        archivo_abierto = open(path, 'w') # w -> write
        texto=""
        for i in marcas:
            texto += i.nombre+"|"+i.pais_origen+"|"+i.fecha_creacion+"|"+i.sucursal_local+"|"+i.valor+"|"+"\n"
        archivo_abierto.write(texto)
        archivo_abierto.close()
    except Exception as Error:
        print("Error leyendo archivo")

def leerMarcas():
    try:
        path = "/home/d/Documentos/programacion/practiva/marcas.txt"
        archivo_abierto = open(path, "r")
        for i in archivo_abierto:
            a=i.split("|")
            marcas.append(Marca_auto(a[0],a[1],a[2],a[3],a[4]))
        archivo_abierto.close()
    except Exception as Error:
        print("Error leyendo archivo")

def menuPrincipal():
    texto ="--------------------------------------"+"\n"
    texto+="-          Menu Principal            -"+"\n"
    texto+="- Registro de Marcas de vehiculos     -"+"\n"
    texto+="- 1. Ingresar una nueva Marca        -"+"\n"
    texto+="- 2. Mostrar las Marcas registradas  -"+"\n"
    texto+="- 3. Modificar una Marca             -"+"\n"
    texto+="- 4. Eliminar una Marca              -"+"\n"
    texto+="- 5. Menu Modelos de vehiculos       -"+"\n"
    texto+="- 6. Salir                           -"+"\n"
    texto+="--------------------------------------"+"\n"    
 
    while True:
        entrada = input(texto)
        try:
            opcion = int(entrada)
        except ValueError as identifier:
            print("ingrese un valor corecto")
            continue

        if(opcion>6 or opcion<1):
            print("ingrese un valor corecto")
            continue
        else:
            break    

    def create():
        agregarMarca()
    def read():
        mostrarMarcas()
    def update():
        actualizarMarcas()
    def delate():
        eliminarMarca()
    def salir():
        guardaMarcas()
        guardaModelos()
        exit()
    def vehiculos():
        while not(menuModelos()==False):
            pass
    def opcionSeleccion():
        opciones = {
            1: create,
            2: read,
            3: update,
            4: delate,
            5: vehiculos,
            6: salir
        }
        return opciones[opcion]()
    return opcionSeleccion()
###########################################################################################################
def agregarVehiculo():
    entradaMarca=input("Ingrese el nombre de la Marca: ")
    estado=False
    for i in marcas:
        if(i.nombre==entradaMarca):
            estado=True
            break
    if(estado):
        nombre=input("Ingresen el nombre del Modelo: ")
        tipo=input("Ingresen que tipo de vehiculo es: ")
        precio_bace=input("Ingresen el precio base: ")
        hibrido=input("Ingresen True o False si es hibrido: ")
        modelos.append(Modelo_auto(nombre,tipo,precio_bace,hibrido,entradaMarca))
    else:
        print("No existe la Marca")

def mostrarVehiculo():
    for i in modelos:
        print(i)

def eliminarVehiculo():
    nombre=input("Ingresen el nombre del Modelo de Vehiculo: ")
    estado=False
    for i in modelos:
        if(nombre== i.nombre):
            modelos.remove(i)
            estado=True
            break    
    if(not estado):
        print("No existe el Modelo")

def actualizarVehiculo():
    nombre=input("Ingresen el nombre del Modelo de Vehiculo: ")
    estado=False
    for i in modelos:
        if(nombre == i.nombre):
            modelos.remove(i)
            agregarVehiculo()
            estado=True
            break
    if(not estado):
        print("No existe el Vehiculo")

def guardaModelos():
    try:
        path = "/home/d/Documentos/programacion/practiva/modelos.txt"
        archivo_abierto = open(path, 'w') # w -> write
        texto=""
        for i in modelos:
            texto += i.nombre+"|"+i.tipo+"|"+i.precio_bace+"|"+i.hibrido+"|"+i.marca+"|"+"\n"
        archivo_abierto.write(texto)
        archivo_abierto.close()
    except Exception as Error:
        print("Error leyendo archivo")

def leerModelos():
    try:
        path = "/home/d/Documentos/programacion/practiva/modelos.txt"
        archivo_abierto = open(path, "r")
        for i in archivo_abierto:
            a=i.split("|")
            modelos.append(Modelo_auto(a[0],a[1],a[2],a[3],a[4]))
        archivo_abierto.close()
    except Exception as Error:
        print("Error leyendo archivo")

def menuModelos():
    texto ="--------------------------------------"+"\n"
    texto+="-       Menu Modelos Vehiculos       -"+"\n"
    texto+="- Registro de Modelos de vehiculos   -"+"\n"
    texto+="- 1. Ingresar una nueva Modelo       -"+"\n"
    texto+="- 2. Mostrar las Modelo registradas  -"+"\n"
    texto+="- 3. Modificar una Modelo            -"+"\n"
    texto+="- 4. Eliminar una Modelo             -"+"\n"
    texto+="- 5. Menu Marcas de vehiculos        -"+"\n"
    texto+="--------------------------------------"+"\n"   
 
    while True:
        entrada = input(texto)
        try:
            opcion = int(entrada)
        except ValueError as identifier:
            print("ingrese un valor corecto")
            continue

        if(opcion>5 or opcion<1):
            print("ingrese un valor corecto")
            continue
        else:
            break    

    def create():
        agregarVehiculo()
    def read():
        mostrarVehiculo()
    def update():
        mostrarVehiculo()
    def delate():
        eliminarVehiculo()
    def modelosVehiculos():        
        return False
    def opcionSeleccion():
        opciones = {
            1: create,
            2: read,
            3: update,
            4: delate,
            5: modelosVehiculos
        }
        return opciones[opcion]()
    return opcionSeleccion()

marcas=[]
modelos=[]
leerMarcas()
leerModelos()

while True:
    menuPrincipal()