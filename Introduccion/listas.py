my_other_list = []
# my_list = list()

#print(len(my_other_list))

my_list = [1, 2, 3]
print(my_list)

# pueden llevar varios tipos de datos
my_list = [1, 11, 2, 3, "yeye"]
my_other_list = ["a", "b", "c"]

print(my_list)
# type me da el tipo de dato
print(type(my_list))

# acceder a la lista
valor = my_list[0]
print(valor)

# cuantos elementos son iguales
valor = my_list.count(1)
print(valor)

suma_listas = my_list + my_other_list
print(suma_listas)

my_list.append("castel")
print(my_list)

my_list.insert(0, "0")
print(my_list)

my_list.reverse()
print(my_list)



