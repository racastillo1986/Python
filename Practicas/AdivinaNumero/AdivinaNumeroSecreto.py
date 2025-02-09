import random


def juego_adivinanza():
    # Generar numero del 1 al 100
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False

    print("Bienvenido al juego de adivinanza de numero!")
    print("Debes adiivnar un numero del 1 al 100")
    print("Go")

    while not adivinado:
        adivinanza = input("Introduzca numero del 1 al 100: ")

        # Verificar el dato ingresado sea numero
        # xq el input lo ingresa por defecto como string
        if adivinanza.isdigit():
            adivinanza = int(adivinanza)
            intentos += 1

            if adivinanza < numero_secreto:
                print(f"El numero secreto es mayor a {adivinanza}")
            elif adivinanza > numero_secreto:
                print(f"El numero secreto es menor a {adivinanza}")
            else:
                print(f"El numero {adivinanza}  es correcto!!!")
        else:
            print("Ingrese un numero valido entre 1 y 100 x dios -.-")

juego_adivinanza()