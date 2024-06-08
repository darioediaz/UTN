"""
Enunciado:

Una compañía famacéutica necesita un programa para procesar los datos de los medicamentos que fabrica. Por cada
medicamento, se tienen los siguientes datos: código de identificación (un entero), nombre del medicamento (una
cadena), el tipo de medicamento (un entero entre 1 y 40 para indicar, por ejemplo: 1: pedíátrico, 2: analgésico,
etc.), el modo de almacenamiento (otro entero, entre 0 y 9 para indicar por ejemplo: 0: en frío, 1: a temperatura
ambiente, 2: sin exposición  a la luz, etc.) y el costo de fabricación (un flotante).  Se pide definir en un módulo
separado el tipo de registro Medicamento con los campos pedidos, y desarrollar en un segundo módulo un programa en
Python controlado por menú de opciones que permita gestionar las siguientes tareas:

1)Cargar un arreglo de registros con los datos de n medicamentos de manera que en todo momento se mantenga ordenado por
código de identificación, de menor a mayor. Para esto debe utilizar el algoritmo de inserción ordenada con búsqueda
binaria (se considerará directamente incorrecta la solución basada en cargar el arreglo completo y ordenarlo al final,
o aplicar el algoritmo de inserción ordenada, pero con búsqueda secuencial). Puede hacer la carga en forma manual
(en cuyo caso realice las validaciones que sean necesarias), o puede generar los datos en forma automática (con valores
aleatorios generados en el rango correcto). Pero si hace carga manual, TODA la carga debe ser manual, y si la hace
automática entonces TODA debe ser automática.

2)Mostrar los datos de los medicamentos (a razón de uno por por línea de pantalla) cuyo costo sea mayor al costo
promedio de todos los registros del arreglo.

3)Usando el arreglo creado en el punto 1, determine la cantidad de medicamentos por cada combinación posible de tipo y
modo de almacenamiento (o sea, 400 contadores: cantidad de medicamentos tipo 1 con modo de almacenamiento 0,  tipo 1
con modo 2, etc.). Genere TODOS los contadores, pero muestre sólo los resultados que correspondan al tipo de
medicamento t que se carga por teclado.

4)Usando el arreglo creado en el punto 1, generar un archivo con todos los medicamentos cuyo modo de almacenamiento
sea  2, 5 o 9. Si el archivo ya existía, eliminar su contenido y comenzar desde cero.

5)Mostrar por pantalla el contenido del archivo creado en el punto anterior. Pero al final del listado, muestre una
línea adicional indicando la cantidad de registros que se mostraron que eran del tipo de medicamento x, cargando x por
teclado.

6)(Además de todos los ítems del 1 al 5 planteados para los alumnos que rinden para regularizar, los alumnos que rindan
para aprobar en forma directa deben agregar una solución para el ítem que sigue): En el menú de opciones del programa,
incluya una opción que permita cargar una cadena de caracteres, y luego pase esa cadena como parámetro a una función
que determine cuántas palabras de la cadena comenzaban con una vocal y tenían al menos un dígito en cualquier posición.
"""
# --------------------------------------------------------------------------------------------------------------- import
from test_funciones2 import *


# ------------------------------------------------------------------------------------------------------- inicio de menu
def test():
    op = 0
    archivo = None
    vec = None
    while op != 7:  # ------------------------------------------------------------------------------------ texto de menu
        menu()
        op = int(input("Ingrese opcion: "))
        if op == 1:  # -------------------------------------------------------------------------------------------- op 1
            vec = []
            n = validar()
            cargar_vector(vec, n)
            mensaje_exito()
        elif op == 2:  # ------------------------------------------------------------------------------------------ op 2
            if vec is not None:
                mostrar_vector(vec)
                mensaje_exito()
            else:
                mensaje_falta_carga()
        elif op == 3:  # ------------------------------------------------------------------------------------------ op 3
            if vec is not None:
                t = int(input("Indique tipo de medicamento a mostrar (1-40): "))
                matriz = cargar_matriz(vec)
                mostrar_matriz(matriz, t)
                mensaje_exito()
            else:
                mensaje_falta_carga()
        elif op == 4:  # ------------------------------------------------------------------------------------------ op 4
            if vec is not None:
                cargar_archivo(vec)
                mensaje_exito()
            else:
                mensaje_falta_carga()
        elif op == 5:  # ------------------------------------------------------------------------------------------ op 5
            if vec is not None:
                x = int(input("Ingrese tipo de medicamento a filtrar (1-40): "))
                mostrar_archivo(archivo, x)
                mensaje_exito()
            else:
                mensaje_falta_carga()
        elif op == 6:  # ------------------------------------------------------------------------------------------ op 6
            pass
        elif op == 7:  # ------------------------------------------------------------------------------------------ op 7
            mensaje_exito()
            break
        else:
            mensaje_error()


# ---------------------------------------------------------------------------------------------------------- fin de menu
if __name__ == "__main__":
    test()
