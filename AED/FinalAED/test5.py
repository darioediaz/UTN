from test_funciones5 import *


def test():
    op = 0
    vec = None
    archivo = None
    while op != 7:
        menu()
        op = int(input("Seleccione opcion: "))
        if op == 1:
            vec = []
            generar_arreglo(vec)
            mensaje_exito()
        elif op == 2:
            if vec is None:
                mensaje_error()
                mensaje_carga()
            else:
                mostrar_arreglo(vec)
                mensaje_exito()
        elif op == 3:
            if vec is None:
                mensaje_error()
                mensaje_carga()
            else:
                archivo = generar_archivo(vec)
                mensaje_exito()
        elif op == 4:
            if vec is None:
                mensaje_error()
                mensaje_carga()
            else:
                mostrar_archivo(archivo)
                mensaje_exito()
        elif op == 5:
            if vec is None:
                mensaje_error()
                mensaje_carga()
            else:
                existe_dni(vec)
                mensaje_exito()
        elif op == 6:
            if vec is None:
                mensaje_error()
                mensaje_carga()
            else:
                matriz = generar_matriz(vec)
                mostrar_matriz(matriz)
                mensaje_exito()
        elif op == 7:
            mensaje_exito()
            break
        else:
            mensaje_error()


if __name__ == "__main__":
    test()
