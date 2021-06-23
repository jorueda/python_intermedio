# filter, map, reduce
from functools import reduce

def listado():
    lista = [1, 4, 5, 6, 9, 13, 19, 21]
    impares1 = [numero for numero in lista if numero % 2 != 0]
    print(impares1)
    # Usando list comprehension

def filtrar():
    lista = [1, 4, 5, 6, 9, 13, 19, 21]
    impares2 = list(filter(lambda x: x%2 != 0, lista))
    print(impares2)
    # La función filter filtra aquellos valores que cumplen la condición. 

def mapear():
    lista = [1, 2, 3, 4, 5]
    cuadrados = list(map(lambda x: x**2, lista))
    print(cuadrados)
    # La función map genera la lista obteniendo el resultado de la fórmula a cada valor.

def reducir():
    lista = [2, 2, 2, 2, 2]
    todos_multiplicados = reduce(lambda a, b: a * b, lista)
    print(todos_multiplicados)
    # La función reduce a un ŕesultado final el acumulado del valor y del anterior. 

if __name__ == '__main__':
    listado()
    filtrar()
    mapear()
    reducir()