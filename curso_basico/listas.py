#lista variable
lista_personas = ["Link", "Zelda", "Kratos"]

#Impresion de la lista
print(lista_personas)
#Impresion por indice
print(lista_personas[0])

#Operaciones de listas
# Modificar elemento
lista_personas[1] = "Racastillo"
print(lista_personas)

# Agregar elemento al final de la lista
lista_personas.append("Luci")
print(lista_personas)

# Insertar elemento en posicion especifica
lista_personas.insert(2,"Loco")
print(lista_personas)

# Eliminar elemeto por valor
lista_personas.remove("Luci")
print(lista_personas)

# Eliminar elemento por indice
del lista_personas[2]
print(lista_personas)

# Longitud de la lista(cant elementos)
longitud = len(lista_personas)
print(longitud)
