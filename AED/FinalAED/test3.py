from test_funciones3 import *

'''Una empresa de vigilancia y seguridad privada requiere un programa que le permita gestionar los datos de los 
servicios que ofrece. De cada Servicio se tiene su código (un entero), su nombre (una cadena), la descripción general 
del mismo (una cadena con un texto terminado en punto y con palabras separadas por un blanco (por ejemplo: 
“Vigilancia integral en barrios cerrados.”), el importe a facturar por ese servicio (un valor de tipo float), 
un número entre 0 y 14 que indica el tipo de servicio (por ejemplo: 0: vigilancia en calles de barrio abierto, 
1: vigilancia perimetral en barrios cerrados, etc.), y otro número, pero entre 0 y 9 para indicar el nivel de riesgo 
que implica ese servicio (por ejemplo: 0: bajo riesgo, 1: riesgo leve, 2: riesgo moderado, etc.). En base a lo 
anterior, desarrollar un programa completo que disponga al menos de dos módulos: • En uno de ellos, definir la clase 
Servicio que represente al registro a usar en el programa, y las funciones básicas para operar con registros de ese 
tipo. Este módulo deberá contener también la definición de cualquier otro tipo de registro que se indique. • En otro 
módulo, incluir el programa principal y las funciones generales que sean necesarias. Para la carga de datos, 
aplique las validaciones que considere necesarias. El programa debe basarse en un menú de opciones para desarrollar 
las siguientes tareas: 1. Generar un arreglo de registros que contenga los datos de todos los servicios. Puede 
generarlo cargando los datos en forma manual o generando los datos en forma aleatoria. El arreglo debe permanecer 
ordenado por el nombre de los servicios en todo momento durante la carga. Debe considerar que esta opción puede ser 
invocada varias veces a lo largo del programa, y que en cada ejecución pueden agregarse tantos registros como desee 
el operador, sin eliminar los datos que ya estaban cargados. Será considerada la eficiencia de la estrategia de carga 
y los algoritmos que aplique. 2. Mostrar el arreglo generado en el punto anterior, a razón de un registro por línea 
en la consola de salida. Al final del listado muestre el importe promedio de todos los registros mostrados. 3. 
Recorra el arreglo que generó en el punto 1, y genere a partir de él un archivo binario de registros, con los datos 
de todos los servicios de ese arreglo en los que el nivel de riego sea mayor a 3. 4. Muestre el archivo creado en el 
punto anterior, y al final del listado agregue una línea adicional indicando la cantidad de registros que se 
mostraron. 5. Determine si existe en el arreglo creado en el punto 1 un servicio cuyo código coincida con el valor 
cod que se carga por teclado. Si existe, muestre sus datos completos, detenga la búsqueda y retorne la cadena 
contenida en el campo descripción de su historial profesional. Si no existe, informe con un mensaje y retorne la 
cadena “No existe.”. 6. A partir del arreglo creado en el punto 1, determine cuántos servicios hay para cada una de 
las posibles combinaciones entre tipo de servicio y y niveles de riesgo (un total de 15 * 10 = 150 contadores). 
Genere todos los contadores posibles, pero muestre solo los resultados que sean diferentes de cero y que correspondan 
a los tipos de servicios mayores al número x que se carga por teclado. 7. Tome la cadena retornada en el punto 5 (si 
existía el registro buscado), y determine cuántas palabras de esa cadena tenían un número impar de caractres, 
y además tenían dos o más veces la combinación "pe". Como se dijo, la cadena debe terminar con un punto y las 
palabras deben separarse entre ellas con un (y solo un) espacio en blanco. La cadena debe ser procesada caracter a 
caracter, a razón de uno por cada vuelta del ciclo que itere sobre ella.'''


def test():
    op = 0
    vec = None
    archivo = None
    while op != 7:
        menu()
        op = int(input("Indique su opcion(1-7): "))
        if op == 1:
            vec = []
            n = int(input("Indique cantidad de arreglos a crear: "))
            generar_arreglo(vec, n)
            mensaje_exito()
        elif op == 2:
            mostrar_arreglo(vec)
            mensaje_exito()
        elif op == 3:
            if vec is not None:
                archivo = generar_archivo(vec)
                mensaje_exito()
            else:
                mensaje_error()
                mensaje_carga_datos()
        elif op == 4:
            if vec is not None:
                mostrar_archivo(archivo)
                mensaje_exito()
            else:
                mensaje_error()
                mensaje_carga_datos()
        elif op == 5:
            if vec is not None:
                cod = int(input("Indique el codigo que desea buscar: "))
                existe_codigo(vec, cod)
                mensaje_exito()
            else:
                mensaje_error()
                mensaje_carga_datos()
        elif op == 6:
            if vec is not None:
                x = int(input("Indique el tipo de servico: "))
                matriz = generar_matriz(vec)
                mostrar_matriz(matriz, x)
                mensaje_exito()
            else:
                mensaje_error()
                mensaje_carga_datos()
        elif op == 7:
            break
        else:
            mensaje_error()


if __name__ == "__main__":
    test()
