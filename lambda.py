suma = lambda a, b: a + b
resultado = suma(2, 5)
print(resultado)

#forma convencional de funciones
"""
def sumas(c, d):
    resultados = c + d
    return resultados

operacion = sumas(2, 5)
print(operacion)
"""
print("**********************")

lista_vacia = lambda lista: len(lista) == 0
print(lista_vacia([2,3,4]))