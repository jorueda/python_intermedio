def run():
    
    # squares = []
    # for contador in range (1, 101):
    #     if contador % 3 != 0:
    #         squares.append(contador ** 2)
    # Lista de numeros al cuadrado divisibles por 3 sin list comprehensions
    
    squares = [contador ** 2 for contador in range(1, 101) if contador % 3 != 0]
    # Lista de numeros divisibles por 3 con list comprehensions
    # Para cada contador en el rango de 1 a 101, va a guardar en la lista numeros al cuadrado solamente
    # si contador es diferente de 0

    listado = [contador for contador in range(1, 100000) if contador % 4 == 0 and contador % 6 == 0 and contador % 9 == 0]

    # List comprehension entregue una lista de todos los múltiplos de 4 que a la vez también son
    # múltiplos de 6 y de 9, hasta 5 dígitos.

    print(squares)
    print(listado)


if __name__ == '__main__':
    run()