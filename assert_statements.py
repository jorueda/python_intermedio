def palindrome(cadena):
    assert len(cadena) > 0, "No se puede ingresar una cadena vacía."
    assert not(cadena.isnumeric()), "Es un número, debes ingresar caracteres."
    
    return cadena == cadena[::-1]

# cadena = input("Ingrese una cadena: ")
# print("¿Es un palíndromo?", palindrome(cadena))


def divisors(numero):
    divisors = [contador for contador in range(1, numero + 1) if numero % contador == 0]
    print(divisors)

def run():
    numero = input("Ingrese un número para obtener los divisores: ")
    assert numero.isnumeric(), "Debes ingresar un número positivo."
    numero = int(numero)
    assert numero != 0, "Debes ingresar un número positivo diferente de 0."
    divisors(numero)
    print("Terminó mi programa.")
    

if __name__ == '__main__':
    run()
