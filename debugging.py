def divisors(numero):
    try:
        if numero < 0:
            raise ValueError("Debes ingresar un número positivo.")
        elif numero == 0:
            raise ValueError("El número no puede ser 0.")
        divisors = [contador for contador in range(1, numero + 1) if numero % contador == 0]
        print(divisors)
    except ValueError as error:
        print(error)

def run():
    try:
        numero = int(input("Ingrese un número para obtener los divisores: "))
        divisors(numero)
        print("Terminó mi programa.")
    except ValueError:
        print("Debe ser de tipo número.")
    

if __name__ == '__main__':
    run()
