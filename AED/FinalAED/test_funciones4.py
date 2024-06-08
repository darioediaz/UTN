import os.path
import pickle
import random

def menu():
    print('''
    Menu:
    1- Genrar arreglo
    2- Mostrar arreglo
    3- Generar archivo
    4- Mostrar archivo
    5- Mostrar archivo filtrado
    6- Existe codigo
    7- Generar y mostrar matriz
    8- Salir
    ''')

def mensaje_exito():
    print("Opcion completada con exito!")

def mensaje_error():
    print("Error! Opcion invalida!")

def mensaje_carga():
    print("Opcion invalida! Debe completar la opcion 1 para continuar...")



class Evento:
    def __init__(self, codigo, titulo, descripcion, costo, tipo, segmento):
        self.codigo = codigo
        self.titulo = titulo
        self.descripcion = descripcion
        self.costo = costo
        self.tipo = tipo
        self.segmento = segmento

def to_string(x):
    return (f"Codigo: {x.codigo:<5} | "
            f"Titulo: {x.titulo:<12} | "
            f"Descripcion: {x.descripcion:<30} | "
            f"Costo: ${x.costo:<7} | "
            f"Tipo: {x.tipo:<5} | "
            f"Segmento: {x.segmento:<5}")

def generar_arreglo(vec):
    n = int(input("Ingrese cantidad de arreglos a crear: "))
    for i in range(n):
        codigo = random.randint(1, 9999)
        titulo = f"Titulo {i}"
        descripcion = f"Es una descrpcion numero {i}."
        costo = float(random.randint(100, 999))
        tipo = random.randint(0, 19)
        segmento = random.randint(0, 9)

        evento = Evento(codigo, titulo, descripcion, costo, tipo, segmento)

        busqueda_binaria(vec, evento)

def busqueda_binaria(vec, dato):
    n = len(vec)
    pos = n
    inicio, final = 0, n - 1
    while inicio <= final:
        centro = (inicio + final) // 2
        if dato.codigo == vec[centro].codigo:
            pos = centro
            break
        elif dato.codigo > vec[centro].codigo:
            inicio = centro +1
        else:
            final = centro - 1

    if inicio > final:
        pos = inicio

    vec[pos:pos] = [dato]

def mostrar_arreglo(vec):
    for item in vec:
        print(to_string(item))

def generar_archivo(vec):
    p = float(input("Ingrese monto a filtar: "))
    m = open("eventos.dat", "wb")
    for item in vec:
        if item.costo >= p:
            pickle.dump(item, m)
    m.close()
    print("Archivo generado con exito!")

def mostrar_archivo(archivo):
    if not os.path.exists("eventos.dat"):
        print("No existe el archivo")
    else:
        m = open("eventos.dat", "rb")
        tamaño = os.path.getsize("eventos.dat")
        while m.tell() < tamaño:
            evento = pickle.load(m)
            print(to_string(evento))
        m.close()

def filtrar_archivo(archivo):
    if not os.path.exists("eventos.dat"):
        print("No existe el archivo")
    else:
        contador, sumador, vec_nuevo = 0, 0, []
        m = open("eventos.dat", "rb")
        tamaño = os.path.getsize("eventos.dat")
        while m.tell() < tamaño:
            evento = pickle.load(m)
            if evento.tipo >= 5:
                contador += 1
                sumador += evento.costo
                vec_nuevo.append(evento.costo)
        m.close()
        promedio = sumador / contador
        print(f"Costos: {vec_nuevo}")
        print(f"El monto promedio en de ${promedio} ")

def existe_cod(vec):
    cod = int(input("Ingrese codigo a filtrar: "))
    existe = False
    for item in vec:
        if item.codigo == cod:
            existe = True
            print(f"Hay coincidencia: \n{to_string(item)}")
            break
    if not existe:
        print("No existe")

def generar_matriz(vec):
    matriz = [[0] * 20 for i in range(10)]

    for item in vec:
        columna = item.tipo
        fila = item.segmento
        matriz[fila][columna] += 1
    return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if i > 7:
                print(f"Tipo: {i:<5} | Segmento {j:<5} | Cantidad: {matriz[i][j]}")

