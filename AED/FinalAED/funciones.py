def test():
    def busqueda_binaria(vec, dato):
        n = len(vec)  # cantidad total de elementos en la lista
        pos = n  # posicion del puntero = al tptal de elementos de la lista

        iz = 0  # inicio de la lista (primer elemento)
        de = n - 1  # final de la lista (ultimo elemento)

        while iz <= de:  # mientras la izquierda sea menor o igual a la derecha, el programa continua
            c = (iz + de) // 2  # centro de la lista (se divide para encontrar el centro de la lista)
            if vec[c] == dato:  # si el dato es igual al centro de la lista, se encontro lo que se buscaba
                pos = c  # entonces la posicion del dato es igual al centro de la lista
                break
            if dato < vec[c]:  # si el dato es menor al centro de la lista, el dato se encuentra en la izq. del dato
                de = c - 1  # entonces el final de la lista ahora es el centro - 1
            else:  # si el dato es mayor al centro de la lista, el dato se encuentra en la derecha del dato
                iz = c + 1  # entonces el inicio de la lista ahora es el centro + 1

        if iz > de:
            pos = iz

        vec[pos:pos] = [dato]

    #  ---------------------------------------------------------------------------------------------------------------------


class Clase:
    def __init__(self, dato1, dato2, dato3):
        self.dato1 = dato1
        self.dato2 = dato2
        self.dato3 = dato3


def convertir_a_cadena(reg):
    return (f"| Dato1: {reg.dato1} "
            f"| Dato2: {reg.dato2} "
            f"| Dato3: {reg.dato3} ")


def prueba():
    reg = Clase(50, "unDato", "otroDato")
    print(convertir_a_cadena(reg))


# ----------------------------------------------------------------------------------------------------------------------

def matriz(lista):  # matriz de 1 * 15 porque acumula cosas
    acumulador = [0] * 15

    for persona in lista:
        acumulador[persona.nombre] += persona.edad
    return acumulador


def mostrar_matriz(acumulador):
    for i in range(len(acumulador)):
        print(f"Nombre: {i:<10} | Edad: {acumulador[i]:<5}")


# ----------------------------------------------------------------------------------------------------------------------

def vector_filtrado(lista):
    nuevo_vector = []

    for elemento in lista:
        if elemento.edad > 20:  # edad > 20 seria la condicion que se pide
            nuevo_vector.append(elemento)

    return nuevo_vector


# ----------------------------------------------------------------------------------------------------------------------

def buscar_por_dato(lista, dato):
    resultado = None
    for elemento in lista:
        if elemento.dato == dato:
            resultado = dato
            break
    return resultado


# ----------------------------------------------------------------------------------------------------------------------
