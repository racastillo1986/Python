diccionario = {'clave1': 'valor1',
               'clave2': 'valor2',
               'clave3': 'valor3'}

print(diccionario)
print(diccionario['clave1'])
print(diccionario.get('clave10', 'No existe clave'))

print(tuple(diccionario.keys()))
print(list(diccionario.values()))
print(len(diccionario))

print("**************Metodos para diccionarios****************")

print("Modificar un elemento")
diccionario['clave1'] = 'valorModificado'
print(diccionario)

print("Agregar un elemento")
diccionario['clave4'] = 'valorNuevo'
print(diccionario)

print("Eliminar elemento por clave")
del diccionario['clave2']
print(diccionario)

print("Eliminar todos los elementos")
diccionario.clear()
print(diccionario)

print("Agregar varios elementos")
diccionario.update({'clave4': 'valor4', 'clave5': 'valor5'})
print(diccionario)