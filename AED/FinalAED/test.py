from test_funciones import *


def test():
    op = 0
    archivo = None
    while op != 8:  # ----------------------------------------------------------------------------------- texto del menu
        menu()
        op = int(input("Ingrese su opcion: "))
        if op == 1:  # -------------------------------------------------------------------------------------------- op 1
            vec = []
            n = int(input("Ingrese cantidad de elementos que contendra el arreglo: "))
            cargar_vector(vec, n)
        elif op == 2:  # ------------------------------------------------------------------------------------------ op 2
            mostrar_vector(vec)
        elif op == 3:  # ------------------------------------------------------------------------------------------ op 3
            archivo = crear_archivo(vec)
        elif op == 4:  # ------------------------------------------------------------------------------------------ op 4
            mostrar_archivo(archivo)
        elif op == 5:  # ------------------------------------------------------------------------------------------ op 5
            dato = int(input("Ingrese el ID que desea buscar: "))
            existe(vec, dato)
        elif op == 6:  # ------------------------------------------------------------------------------------------ op 6
            pass
        elif op == 7:  # ------------------------------------------------------------------------------------------ op 7
            matriz = cargar_matriz(vec)
            mostrar_matriz(matriz)
        elif op == 8:  # ------------------------------------------------------------------------------------------ op 8
            pass
        elif op == 9:
            print("Gracias!")
            break
        else:
            print("Error, opcion invalida!")


# ---------------------------------------------------------------------------------------------------------- fin de menu
if __name__ == "__main__":
    test()
