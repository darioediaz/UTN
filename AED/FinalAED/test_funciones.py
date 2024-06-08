"""
Un centro de investigación necesita un programa que le permita trabajar con los datos de los diferentes proyectos que
están registrados en él. De cada Proyecto, se tiene un número de identificación (un número entero), su nombre o título
(una cadena), la descripción breve del objetivo del proyecto (una cadena con un texto terminado en punto y con palabras
separadas por un blanco, el monto asignado al desarrollo del proyecto, un número entre 1 y 39 que indica el área de
aplicación (por ejemplo: 1: Medicina, 2: Biología, 3: Ingeniería, etc.), y otro número, pero entre 0 y 9 para indicar
el tipo de proyecto (por ejemplo: 0: Incentivo para nuevos investigadores, 1: De interés provincial, 2: De interés
naciional, etc.).  En base a lo anterior, desarrollar un programa completo que disponga al menos de dos módulos:

• En uno de ellos, definir la clase Proyecto que represente al registro a usar en el programa, y las funciones básicas
para operar con registros de ese tipo.
• En otro módulo, incluir el programa principal y las funciones generales que sean necesarias.
Para la carga de datos, aplique las validaciones que considere necesarias. El programa debe basarse en un menú de
opciones para desarrollar las siguientes tareas:

1. Generar un arreglo de registros que contenga los datos de todos los proyectos. Puede generarlo cargando los datos en
forma manual o generando los datos en forma aleatoria. El arreglo debe permanecer ordenado por número de identificación
en todo momento durante la carga (será especialmente considerada la eficiencia de la estrategia que aplique).
Debe tener en cuenta que esta opción debe poder ser invocada varias veces a lo largo del programa, y que en cada
ejecución se debe poder agregar tantos registros como desee el operador, sin eliminar los datos que ya estaban
cargados.

2. Mostrar el arreglo generado en el punto anterior, a razón de un registro por línea en la consola de salida.

3. A partir del arreglo, generar un archivo binario de registros que contenga los datos de todos los proyectos cuyo
tipo no sea ni 0 ni 1. Cada vez que esta opción se seleccione, el archivo debe crearse otra vez, eliminando los
anteriores registros que hubiese contenido.

4. Mostrar todos los datos del archivo que generó en el punto 3, a razón de un registro por línea, pero agregue al
final del listado una línea adicional indicando el monto promedio de todos los registros que se mosgtraron.

5. Determine si existe en el arreglo creado en el punto 1 un proyecto en el que su número de identificación coincida
con el valor num que se carga por teclado. Si existe, muestre sus datos completos y detenga la búsqueda.
Si no existe, informe con un mensaje.

6. Recorra el arreglo y cree una cadena que contenga la concatenación de todos los textos contenidos en el campo
objetivo de todos los registros en los que la longitud de la cadena contenida en ese campo sea mayor a 10. La cadena
creada solo debe contener UN punto al final, y debe cumplirse que las palabras sigan separadas entre ellas por un y
solo un espacio en blanco. Retorne la cadena creada, o retorne una cadena de la forma ‘Imposible.’ si ningún registro
cumplía la condición pedida. En ambos casos, muestre la cadena retornada.

7. A partir del arreglo, determine cuántos proyectos existen para cada una de las posibles combinaciones entre áreas
de aplicación y tipos de proyectos (un total de 40 * 10 = 400 contadores). Muestre los resultados que sean diferentes
a cero, pero solo para los contadores que correspondan a áreas mayores a 10.

8. Tome la cadena retornada en el punto 6, y determine cuántas palabras de esa cadena contenían al menos dígito y al
menos una vez la combinación de dos vocales seguidas (por ejemplo: "aerosol98" o "x4solsticio" ).  Como se dijo, la
cadena debe terminar con un punto y las palabras deben separarse entre ellas con un (y solo un) espacio en blanco.
La cadena debe ser procesada caracter a caracter, a razón de uno por cada vuelta del ciclo que itere sobre ella,
al estilo usual.
"""
# imports --------------------------------------------------------------------------------------------------------------
import os.path
import pickle
import random


# texto del menu -------------------------------------------------------------------------------------------------------
def menu():
    print('''
            1 - Generar arreglo
            2 - Mostrar arreglo
            3 - Generar archivo binario
            4 - Mostrar archivo
            5 - Buscar ID en arreglo y mostrarlo
            6 - Crear cadena
            7 - Contar las combinaciones de areas y tipo
            8 - Procesar cadena
            9 - Salir
            ''')


# punto 1 --------------------------------------------------------------------------------------------------------------
class Proyecto:
    def __init__(self, id, nombre, descripcion, monto, area, tipo):
        self.id = id
        self.nombre = nombre
        self.descripcion = descripcion
        self.monto = monto
        self.area = area
        self.tipo = tipo


def to_string(reg):
    return (f"ID: {reg.id:<7}| "
            f"Nombre: {reg.nombre:<12}| "
            f"Descripcion: {reg.descripcion:<42}| "
            f"Monto: ${reg.monto:<5}| "
            f"Area: {reg.area:<4}| "
            f"Tipo: {reg.tipo:<3} ")


def cargar_vector(vec, n):
    for i in range(n):
        id = random.randint(0000, 9999)
        nombre = f"Nombre {i}"
        descripcion = f"Esta es una breve descripcion numero {i}."
        monto = random.randint(100, 999)
        area = random.randint(1, 39)
        tipo = random.randint(0, 9)

        proyecto = Proyecto(id, nombre, descripcion, monto, area, tipo)

        busqueda_binaria(vec, proyecto)


def busqueda_binaria(vec, dato):
    n = len(vec)
    x = n
    inicio = 0
    fin = n - 1
    while inicio <= fin:
        centro = (inicio + fin) // 2
        if dato.id == vec[centro].id:
            x = centro
            break
        elif dato.id > vec[centro].id:
            inicio = centro + 1
        else:
            fin = centro - 1

    if inicio > fin:
        x = inicio

    vec[x:x] = [dato]


# punto 2 --------------------------------------------------------------------------------------------------------------
def mostrar_vector(vec):
    for i in vec:
        print(to_string(i))


# punto 3 --------------------------------------------------------------------------------------------------------------
def crear_archivo(vec):
    m = open("proyecto.dat", 'wb')
    contador = 0
    for i in vec:
        if i.tipo > 1:
            contador += 1
            pickle.dump(i, m)
    if contador > 0:
        print(f"El archivo se creó con {contador} registros")
    m.close()


# punto 4 --------------------------------------------------------------------------------------------------------------
def mostrar_archivo(archivo):
    m = open("proyecto.dat", 'rb')
    tam = os.path.getsize("proyecto.dat")
    while m.tell() < tam:
        proyecto = pickle.load(m)
        print(to_string(proyecto))
    m.close()


# punto 5 --------------------------------------------------------------------------------------------------------------
def existe(vec, dato):
    existe = False
    for i in vec:
        if dato == i.id:
            existe = True
            break
    if existe:
        print(f"Se ha encontrado coincidencia y es la siguiente: \n{to_string(i)}")
    else:
        print("No se ha encontrado coincidencia")


# punto 6 --------------------------------------------------------------------------------------------------------------


# punto 7 --------------------------------------------------------------------------------------------------------------
def cargar_matriz(vec):
    matriz = [[0] * 40 for i in range(10)]
    for i in vec:
        columna = i.area - 1
        fila = i.tipo - 1
        matriz[fila][columna] += 1
    return matriz


def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != 0 and matriz[i][j] > 10:
                print(f"Tipo: {j + 1:<4} | Area: {i + 1:<4} | Cantidad: {matriz[i][j]:<4}")

# punto 8 --------------------------------------------------------------------------------------------------------------
