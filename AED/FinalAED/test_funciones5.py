import os.path
import pickle
import random


def menu():
    print('''
    Menu:
    1- Generar arreglo
    2- Mostrar arreglo
    3- Generar archivo
    4- Mostrar archivo
    5- Existe DNI
    6- Generar y mostrar matriz
    7- Salir
    ''')


def mensaje_exito():
    print("Opcion completada con exito!")


def mensaje_error():
    print("Error! Opcion invalida!")


def mensaje_carga():
    print("Debe completar la opcion 1!")


class Nutricioista:
    def __init__(self, dni, nombre, descripcion, sueldo, universidad, tipo):
        self.dni = dni
        self.nombre = nombre
        self.descripcion = descripcion
        self.sueldo = sueldo
        self.universidad = universidad
        self.tipo = tipo


def to_string(x):
    return (f"DNI: {x.dni:<10} | "
            f"Nombre: {x.nombre:<12} | "
            f"Descripcion: {x.descripcion:<30} | "
            f"Sueldo: {x.sueldo:<10} | "
            f"Universidad: {x.universidad:<5} | "
            f"Tipo: {x.tipo:<5}")


def generar_arreglo(vec):
    n = int(input("Ingrese cantidad de arreglos a generar: "))
    for i in range(n):
        dni = random.randint(1, 99999999)
        nombre = f"Nombre {i}"
        descripcion = f"Una descripcion numero {i}."
        sueldo = float(random.randint(100, 999))
        universidad = random.randint(0, 19)
        tipo = random.randint(0, 9)

        nutricionista = Nutricioista(dni, nombre, descripcion, sueldo, universidad, tipo)

        add_in_order(vec, nutricionista)


def add_in_order(vec, dato):
    n = len(vec)
    pos = n
    inicio = 0
    final = n - 1
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
    for i in vec:
        print(to_string(i))


def generar_archivo(vec):
    m = open("nutri.dat", "wb")
    for i in vec:
        pickle.dump(i, m)
    m.close()


def mostrar_archivo(archivo):
    if not os.path.exists("nutri.dat"):
        print("El archivo no existe")
    else:
        m = open("nutri.dat", "rb")
        tamaño = os.path.getsize("nutri.dat")
        contador = 0
        sumador = 0
        while m.tell() < tamaño:
            nutricionista = pickle.load(m)
            contador += 1
            sumador += nutricionista.sueldo
            print(to_string(nutricionista))
        m.close()
        print(f"El promedio de sueldos es de: ${sumador / contador}")


def existe_dni(vec):
    dni = int(input("Ingrese DNI a buscar: "))
    existe = False
    for i in vec:
        if i.dni == dni:
            existe = True
            print(f"Hay coincidencia: \n{i.descripcion}")
            break
    if not existe:
        print("No existe")


def generar_matriz(vec):
    matriz = [[0] * 20 for i in range(10)]
    for i in vec:
        columna = i.universidad
        fila = i.tipo
        matriz[fila][columna] += 1
    return matriz


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j > 10:
                print(f"Tipo: {i:<5} | Universidad: {j:<5} | Cantidad: {matriz[i][j]}")
