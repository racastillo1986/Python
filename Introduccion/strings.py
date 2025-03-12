# Strings
my_string = "Hola es un string"
my_string2 = 'Todo belen'
print(my_string)
print(my_string2)

print("longitud del contenido")
print(len(my_string))
print(len(my_string2))

print(my_string + " " + my_string2)

# Salto de linea
string_salto_linea = "Hola \ntodo bien"
print(string_salto_linea)

# Formateo
name, surname, age = "Ramiro", "Castillo", 38
print("Nombre completo: {} {} y mi edad es: {}".format(name, surname, age))
print("Mi nmbre es %s %s y mi edad es: %d" %(name,surname,age))
print(f"Miiii nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres
language = "Python"
a, b, c, d ,e, f = language
print(a)
print(b)
print(c)


# Divisiones
language_slice = language[1:3]
print(language_slice)

language_slice = language[1:]
print(language_slice)

language_slice = language[:3]
print(language_slice)

language_slice = language[-2]
print(language_slice)

# Reverse
reversed_languaje = language[::-1]
print(reversed_languaje)