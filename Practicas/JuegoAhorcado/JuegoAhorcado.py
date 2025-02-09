import random

def obtener_palabra_secreta() -> str:
    palabras = ['python', 'javascript', 'java', 'angular', 'django', 'git']
    return random.choice(palabras)

def mostrar_progreso(palabra_secreta, letras_adivinadas):
    adivinado = ''

    for letra in palabra_secreta:
        if letra in letras_adivinadas:
            adivinado += letra
        else:
            adivinado += "_"
    return adivinado

def juego_ahoracdo():
    palabra_secreta = obtener_palabra_secreta()
    letras_adivinadas = []
    intentos = 10
    juego_terminado = False


    print("Bienvenido al juego del ahorcado!!")
    print(f"Tienes {intentos} intentos para adivinar la palabra secreta")
    print(mostrar_progreso(palabra_secreta, letras_adivinadas))

    while not juego_terminado:
        adivinanza = input("Introduce una letra: ").lower()

        if len(adivinanza) != 1 or not adivinanza.isalpha():
            print("Solo letras")
        elif adivinanza in letras_adivinadas:
            print("Otra no la misma")
        else:
            letras_adivinadas.append(adivinanza)

            if adivinanza in palabra_secreta:
                print(f"Muy bien la letra {adivinanza} esta eln la palabra")
            else:
                intentos -= 1
                print("Letra Fail")
                print(f"Te quedan {intentos} intentos")

        progreso_actual = mostrar_progreso(palabra_secreta, letras_adivinadas)
        print(progreso_actual)

        if "_" not in progreso_actual:
            juego_terminado = True
            print(f"Ganaste la palabra completa es: {palabra_secreta}")

    if intentos == 0:
        print(f"La palabra secreta era: {palabra_secreta}")

juego_ahoracdo()