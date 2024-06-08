import random
from soporte import *


def validar():
    n = int(input('Ingrese la cantidad de servicios a cargar (mayor a cero): '))
    while n <= 0:
        n = int(input('Error... Se pidió mayor a cero... Ingrese nuevamente la cantidad (mayor a cero): '))
    return n


def add_in_order(vec, t):
    n = len(vec)
    izq = 0
    der = n - 1
    while izq <= der:
        c = (izq + der) // 2
        if t.codigo == vec[c].codigo:
            pos = c
            break
        elif t.codigo < vec[c].codigo:
            der = c - 1
        else:
            izq = c + 1

    if izq > der:
        pos = izq

    vec[pos:pos] = [t]


def cargar_arreglo():
    nombres = ("Juan", "Ana", "Luis", "Carla", "Pedro", "Diana", "Matias", "Sandra", "Jose", "Maria", "Lucas")
    apellidos = ("Perez", "Gomez", "Suarez", "Dimarco", "Franceschi", "Tomasini", "Quispe", "Mamani", "Smith", "Evans")
    vec = []
    n = validar()
    for i in range(n):
        cod = random.randint(1, 99999)
        des = "Servicio " + random.choice("ABCDEFGHIJKLMNÑOPQRSTUVWXYZ") + str(random.randint(1,9))
        cli = random.choice(nombres) + " " + random.choice(apellidos)
        tip = random.randint(1, 30)
        mon = round(random.uniform(0, 9000000), 2)

        t = Servicio(cod, des, cli, tip, mon)
        add_in_order(vec, t)
    return vec


def mostrar_arreglo(vec):
    print('Listado completo de servicios ofrecidos')
    for servicio in vec:
        print(servicio)


def principal():
    vec = []
    archivo = None
    opcion = -1
    while opcion != 7:
        print('----------------------- Menú de opciones - Servicios Agropecuarios -------------------------')
        print('1. Cargar arreglo (ordenado por código de servicio)')
        print('2. Mostrar arreglo completo')
        print('3. Buscar por código de servicio')
        print('4. Conteo por tipo de servicio')
        print('5. Generar archivo con condición de filtro')
        print('6. Mostrar archivo (incluir promedio al final)')
        print('7. Salir')
        print('--------------------------------------------------------------------------------------------')
        opcion = int(input('Ingrese número de opción: '))

        if opcion == 1:
            vec = cargar_arreglo()
            print("Carga finalizada - Arreglo generado")
            print()

        elif opcion == 2:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                mostrar_arreglo(vec)
                print()

        elif opcion == 3:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                # TAREA del estudiante...
                cod = int(input('Ingrese el codigo que desea buscar: '))
                busqueda_binaria(vec, cod)

        elif opcion == 4:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                # TAREA del estudiante...
                mostrar_matriz(vec)

        elif opcion == 5:
            if not vec:
                print('El arreglo no ha sido cargado todavía..')
            else:
                # TAREA del estudiante...
                m = float(input('Ingrese monto como limite inferior de busqueda: '))
                archivo = cargar_archivo(vec, m)

        elif opcion == 6:
            # TAREA del estudiante...
            mostrar_archivo(archivo)


if __name__ == '__main__':
    principal()
