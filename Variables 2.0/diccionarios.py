#creando diccionario con dict()
diccionario = dict(nombre = "ramiro", apellido = "castillo")

#forma convencional como in json
#diccionario = {'nombre': "javier", 'apellido': "mcfly"}
print(diccionario)

#Las tuplas pueden ser claves
diccionario = {("yeye", "yeye2"):"jajaja"}
print(diccionario)

#Los conjuntos pueden ser claves con frozenset
diccionario = {frozenset(["yeye", "yeye2"]):"jajaja"}
print(diccionario)

#creando diccionarios con fromkeys()
#crea las claves con valor none
diccionario = dict.fromkeys(["nombre", "apellido"])
print(diccionario["nombre"])

#otro caso pero con un string para que cree una clave por cada caracter
#si le pongo un 2do parametro se lo asigna como valor a cada clave
diccionario = dict.fromkeys("ABCD", "valor")
print(diccionario)

# otro caso
diccionario = dict.fromkeys(["nombre", "apellido"], "valor")
print(diccionario)