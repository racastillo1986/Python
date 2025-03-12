'''
lambda argumentos: expresión

Donde:
argumentos es la lista de parámetros que la función va a recibir (separados por comas, igual que en una función normal).
expresión es el valor que se devuelve cuando la función se ejecuta.
'''


# funcion convencional
def sumar(x, y):
    return x + y
print(sumar(3, 4))  # Salida: 7

# funcion lambda
sumar = lambda x, y: x + y
print(sumar(3, 4))  # Salida: 7
# ---------------------------------------------
# ---------------------------------------------
# Usando lambda con map para multiplicar cada elemento de la lista por 2
numeros = [1, 2, 3, 4, 5]
resultado = list(map(lambda x: x * 2, numeros))
print(resultado)  # Salida: [2, 4, 6, 8, 10]

# Usando lambda con filter para obtener los números pares
numeros = [1, 2, 3, 4, 5, 6]
resultado = list(filter(lambda x: x % 2 == 0, numeros))
print(resultado)  # Salida: [2, 4, 6]

# Usando lambda con sorted para ordenar por el segundo valor de una tupla
tuplas = [(1, 3), (2, 2), (3, 1)]
resultado = sorted(tuplas, key=lambda x: x[1])
print(resultado)  # Salida: [(3, 1), (2, 2), (1, 3)]

