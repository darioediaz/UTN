import random

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21]


# ----------------------------------------------------------------------------------------------------------------------
def busqueda_binaria(lista, dato):
    n = len(lista)
    posicion = n
    inicio = 0
    final = n - 1
    while inicio <= final:
        centro = (inicio + final) // 2
        if dato == centro:
            posicion = centro
            break
        elif dato > centro:
            inicio = centro + 1
        else:
            final = centro - 1
    if inicio > final:
        posicion = inicio
    lista[posicion:posicion] = [dato]


# ----------------------------------------------------------------------------------------------------------------------
def ordenar(lista):  # quicksort
    n = len(lista)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]


# ----------------------------------------------------------------------------------------------------------------------
class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad


def to_string(clase):
    return f"Nombre: {clase.nombre:<10} | Apellido: {clase.apellido:<10} | Edad: {clase.edad:<5}"


'''def show_string():
    clase = Persona("Dario", "Diaz", 32)
    print(to_string(clase))'''


def show_string():
    n = 10
    nom = "Dario", "Yamila", "Justina", "Vittorio", "Roma"
    ape = "Diaz", "Arias", "Grosso"
    for i in range(n):
        nombre = random.choice(nom)
        apellido = random.choice(ape)
        edad = random.randint(1, 90)

        persona = Persona(nombre, apellido, edad)

        print(to_string(persona))


# ----------------------------------------------------------------------------------------------------------------------
if __name__ == "__main__":
    show_string()
