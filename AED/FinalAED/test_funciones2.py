# ------------------------------------------------------------------------------------------------------------------ aux
import os.path
import pickle
import random


def menu():
    print('''
    Menu de opciones:
    1 - Cargar vector
    2 - Mostrar vector
    3 - Crear y mostrar matriz
    4 - Crear archivo
    5 - Mostrar archivo
    6 - Cargar cadena
    7 - Cerrar menu
    ''')


def mensaje_exito():
    print("Opcion completada con exito!")


def mensaje_error():
    print("Error! Opcion invalida!")


def mensaje_falta_carga():
    print("Error! Primero debe cargar los datos en la opcion 1")


def validar():
    n = int(input("Indique cantidad de arreglos a crear: "))
    while n <= 0:
        n = int(input("Error! Al menos debe crear 1 arreglo, intente nuevamente: "))
    return n


# ---------------------------------------------------------------------------------------------------- creacion de clase
class Medicamento:
    def __init__(self, id, nombre, tipo, modo, costo):
        self.id = id  # int
        self.nombre = nombre    # str
        self.tipo = tipo        # int (1...40)
        self.modo = modo        # int (0...9)
        self.costo = costo      # float


def to_string(reg):
    return (f"ID: {reg.id:<5} | "
            f"Nombre: {reg.nombre:<12} | "
            f"Tipo: {reg.tipo:<5} | "
            f"Modo: {reg.modo:<4} | "
            f"Costo: ${reg.costo:<5} ")


# ----------------------------------------------------------------------------------------------------------------- op 1
def busqueda_binaria(vec, dato):
    n = len(vec)
    pos = n
    inicio = 0
    final = n - 1

    while inicio <= final:
        centro = (inicio + final) // 2
        if dato.id == vec[centro].id:
            pos = centro
            break
        elif dato.id > vec[centro].id:
            inicio = centro + 1
        else:
            final = centro - 1

    if inicio > final:
        pos = inicio

    vec[pos:pos] = [dato]


def cargar_vector(vec, n):
    for i in range(n):
        id = random.randint(000, 999)
        nombre = f"Nombre {i}"
        tipo = random.randint(1, 40)
        modo = random.randint(0, 9)
        costo = float(random.randint(100, 999))

        medicamento = Medicamento(id, nombre, tipo, modo, costo)

        busqueda_binaria(vec, medicamento)


# ----------------------------------------------------------------------------------------------------------------- op 2
def mostrar_vector(vec):
    for item in vec:
        print(to_string(item))


# ----------------------------------------------------------------------------------------------------------------- op 3
def cargar_matriz(vec):
    matriz = [[0] * 10 for i in range(40)]
    for item in vec:
        columna = item.modo
        fila = item.tipo - 1
        matriz[fila][columna] += 1
    return matriz


def mostrar_matriz(matriz, t):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i + 1 == t:
                print(f"Tipo: {i + 1:<4} | Modo: {j:<4} | Cantidad: {matriz[i][j]}")
                # print(f"matriz[i] = {matriz[i]}")
                # print(f"i = {i+1}")


# ----------------------------------------------------------------------------------------------------------------- op 4
def cargar_archivo(vec):
    m = open("Medicamentos.dat", 'wb')
    contador = 0
    for i in vec:
        if i.modo == 2 or i.modo == 5 or i.modo == 9:
            contador += 1
            pickle.dump(i, m)
    if contador > 0:
        print(f"El archivo se creó con {contador} registros")
    m.close()


# ----------------------------------------------------------------------------------------------------------------- op 5
def mostrar_archivo(archivo, x):
    if not os.path.exists("servicios.dat"):
        print("No existe el archivo")
    else:
        m = open("Medicamentos.dat", 'rb')
        tam = os.path.getsize("Medicamentos.dat")
        contador = 0
        while m.tell() < tam:
            medicamento = pickle.load(m)
            print(to_string(medicamento))
            if medicamento.tipo == x:
                contador += 1
        print(f"Se encontraron {contador} medicamentos de tipo {x}")
        m.close()

# ----------------------------------------------------------------------------------------------------------------- op 6
