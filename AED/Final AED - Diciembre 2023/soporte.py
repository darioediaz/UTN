import os.path
import pickle


class Servicio:
    def __init__(self, cod, des, cli, tip, mon):
        self.codigo = cod
        self.descripcion = des
        self.cliente = cli
        self.tipo = tip
        self.monto = mon

    def __str__(self):
        cad = 'Codigo: {:<6} | Descripción: {:<20} |  Cliente: {:<20} |  Tipo: {:<2} |  Monto: {:<10}'
        return cad.format(self.codigo, self.descripcion, self.cliente, self.tipo, self.monto)

# --------------------------------------------------------------------------------------------------------- MENU PUNTO 3 - busqueda secuencial
'''def buscar_por_codigo(vec, cod):
    for i in vec:
        if i.codigo == cod:
            existe = True
            print('El codigo existe y es el siguiente:')
            print(i)
            if i.tipo > 4:
                i.monto += 100000
                print('Monto nuevo luego de la modificacion: ', i.monto)
            break
        else:
            existe = False
    if not existe:
        print('No existe el codigo ingresado')'''
# --------------------------------------------------------------------------------------------------------- MENU PUNTO 3 - busqueda binaria
def busqueda_binaria(vec, cod):
    n = len(vec)
    inicio = 0
    final = n-1
    while inicio <= final:
        puntero = (inicio + final) // 2
        existe = False
        if cod == vec[puntero].codigo:
            existe = True
            print('El codigo existe y es el siguiente: ')
            print(vec[puntero])
            if vec[puntero].tipo > 4:
                vec[puntero].monto += 100000
                print('El nuevo monto modificado es ', vec[puntero].monto)
            break
        elif cod > vec[puntero].codigo:
            inicio = puntero + 1
        else:
            final = puntero - 1
    if not existe:
        print('No existe el codigo buscado')

# --------------------------------------------------------------------------------------------------------- MENU PUNTO 4
def cargar_matriz(vec):
    matriz = [[0] * 29 for i in range(1)]
    for i in range(len(vec)):
        fila = vec[i].tipo
        columna = vec[i].monto
        matriz[fila][columna] += 1
        return matriz

def mostrar_matriz(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[j] > 0:
                    print("Tipo de servicio: ", i, ", Monto: ", j, " : ", matriz[i][j])
# --------------------------------------------------------------------------------------------------------- MENU PUNTO 5
def cargar_archivo(vec, m):
    x = open('servicio.dat', 'wb')
    for i in range(len(vec)):
        if m > vec[i].monto:
            pickle.dump(vec[i], x)
    x.close()
    print('Archivo cargado con exito!')
# --------------------------------------------------------------------------------------------------------- MENU PUNTO 6
def mostrar_archivo(archivo):
    if not os.path.exists('servicio.dat'):
        print('No existe el archivo')
    else:
        x = open('servicio.dat', 'rb')
        tam = os.path.getsize('servicio.dat')

        while x.tell() < tam:
            servicio = pickle.load(x)
            print(servicio)
        x.close()
