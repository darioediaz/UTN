import os.path
import pickle
import random

def mensaje_exito():
    print("Opcion completada con exito!")

def mensaje_error():
    print("Error! Opcion invalida!")

def mensaje_carga_datos():
    print("Debe completar la opcion 1")

def menu():
    print('''
    Menu de opciones:
    1 - Generar arreglo
    2 - Mostrar arreglo
    3 - Geerar archivo
    4 - Mostrar archivo
    5 - Buscar por codigo
    6 - Generar matriz
    7 - Salir
    ''')

class Servicio:
     def __init__(self, codigo, nombre, descripcion, importe, tipo, riesgo):
         self.codigo = codigo
         self.nombre = nombre
         self.descripcion = descripcion
         self.importe = importe
         self.tipo = tipo
         self.riesgo = riesgo

def to_string(clase):
    return (f"Codigo: {clase.codigo:<5} | "
            f"Nombre: {clase.nombre:<10} | "
            f"Descripcion: {clase.descripcion:<30} | "
            f"Importe: ${clase.importe:<5} | "
            f"Tipo: {clase.tipo:<5} | "
            f"Riesgo: {clase.riesgo:<5}")

def generar_arreglo(vec, n):
    for i in range(n):
        codigo = random.randint(1000, 9999)
        nombre = f"Nombre {i}"
        descripcion = f"Esta es una descripcion id{i}."
        importe = float(random.randint(100, 999))
        tipo = random.randint(0, 14)
        riesgo = random.randint(0, 9)

        servicio = Servicio(codigo, nombre, descripcion, importe, tipo, riesgo)

        busqueda_binaria(vec, servicio)
def busqueda_binaria(vec, dato):
    n = len(vec)
    pos = n
    inicio, final = 0, n-1

    while inicio <= final:
        centro = (inicio + final) // 2
        if dato.nombre == vec[centro].nombre:
            pos = centro
            break
        elif dato.nombre > vec[centro].nombre:
            inicio = centro + 1
        else:
            final = centro - 1

    if inicio > final:
        pos = inicio

    vec[pos:pos] = [dato]

def mostrar_arreglo(vec):
    contador = 0
    suma = 0
    for item in vec:
        print(to_string(item))
        suma += item.importe
        contador += 1
    promedio = suma / contador
    print(f"el promedio de importes es de: ${promedio}")

def generar_archivo(vec):
    m = open("servicios.dat", "wb")
    contador = 0
    for item in vec:
        if item.riesgo > 3:
            pickle.dump(item, m)
            contador += 1
    m.close()
    if contador > 0:
        print(f"Se han generado {contador} arreglos")

def mostrar_archivo(archivo):
    if not os.path.exists("servicios.dat"):
        print("No existe el archivo")
    else:
        m = open("servicios.dat", "rb")
        tamaño = os.path.getsize("servicios.dat")
        contador = 0
        while m.tell() < tamaño:
            contador += 1
            servicio = pickle.load(m)
            print(to_string(servicio))
        m.close()
        if contador > 0:
            print(f"Se han generado {contador} arreglos con Nivel de Riesgo mayor a 3")

def existe_codigo(vec, cod):
    existe = False
    for item in vec:
        if item.codigo == cod:
            existe = True
            print(f"Hay coincidencia, el item es el siguiente: \n {item.descripcion:<30}")
            break

    if not existe:
        print("No existe")
def generar_matriz(vec):
    matriz = [[0] * 15 for i in range(10)]

    for item in vec:
        columna = item.tipo
        fila = item.riesgo
        matriz[fila][columna] += 1
    return matriz

def mostrar_matriz(matriz, x):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] > 0 and i == x:
                print(f"Tipo: {j:<5} | Riesgo: {i:<5} | Cantidad: {matriz[i][j]:<5}")
