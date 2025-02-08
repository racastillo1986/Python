"""
set() utiliza iterable; una lista x ejemplo
"""

#crando conjunto con set
conjunto = set(["Dato 1"])

#metiendo un conjunto dentro de otro conjunto
"""
frozenset me permite transformar el conjunto a un 
conjunto inmutable para poder meterlo dentro de otro conjunto
"""
conjunto1 = frozenset(["Dato 1", "Dato 2"])
conjunto2 = {conjunto1, "Dato 3"}

print(conjunto2)

#Teoria de conjuntos
conjunto1 = {1, 3, 5, 7}
conjunto2 = {1, 3, 7}

#determinar es subconjunto uno del otro
resultado = conjunto2.issubset(conjunto1)
#otra forma
# el menor o igual q en este caso reemplaza al issubset()
resultado = conjunto2 <= conjunto1

#determinar es superconjunto uno del otro
resultado = conjunto2.issuperset(conjunto1)
#otra forma
# el mayor o igual q en este caso reemplaza al issuperset()
resultado = conjunto2 > conjunto1
print(resultado)