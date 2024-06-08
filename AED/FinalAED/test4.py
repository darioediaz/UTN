from test_funciones4 import *
def test():
    op = 0
    vec, archivo = None, None
    while op != 8:
        menu()
        op = int(input("Ingrese opcion: "))
        if op ==1:
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
                filtrar_archivo(archivo)
                mensaje_exito()
        elif op == 6:
            if vec is None:
                mensaje_error()
                mensaje_carga()
            else:
                existe_cod(vec)
                mensaje_exito()
        elif op == 7:
            if vec is None:
                mensaje_error()
                mensaje_carga()
            else:
                matriz = generar_matriz(vec)
                mostrar_matriz(matriz)
                mensaje_exito()
        elif op == 8:
            break
        else:
            mensaje_error()


if __name__ =="__main__":
    test()