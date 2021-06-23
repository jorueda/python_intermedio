def run():
    my_list = [1, "Hello", True, 4.5]
    my_dict = {"firstname": "Facundo", "lastname": "García"}

    super_list = [ # Lista de dicciionarios
        {"firstname": "Facundo", "lastname": "García"},
        {"firstname": "Miguel", "lastname": "Torres"},
        {"firstname": "Pepe", "lastname": "Rodelo"},
        {"firstname": "Susana", "lastname": "Martínez"},
        {"firstname": "José", "lastname": "García"}
    ]

    super_dict = { # Diccionario de listas
        "natural_nums": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 4.5, 6.43],
    }

    for key, value in super_dict.items():
        print(key, "-", value)

    # Imprimir las llaves y el valor
    for lista in super_list:
        for key, value in lista.items():
            print(key, ":" , value)

    # Imprimir el valor que contiene la llave
    for lista in super_list:
        print(lista["firstname"], lista["lastname"])


if __name__ == '__main__':
    run()