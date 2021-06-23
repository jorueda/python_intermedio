def palindrome(frase):
    try:
        if len(frase) == 0:
            raise ValueError("No se puede ingresar una cadena vacía.")
        return frase == frase[::-1]
    except ValueError as error:
        print(error)
        return False

try:
    print(palindrome(""))
except TypeError:
    print("Sólo se pueden ingresar strings.")