def run():

    diccionario = {contador: contador ** 3 for contador in range(1, 101) if contador % 3 != 0}
    print(diccionario)

    raiz_cuadrada = {contador: contador ** 0.5 for contador in range(1, 1001)}
    print(raiz_cuadrada)


if __name__ == '__main__':
    run()