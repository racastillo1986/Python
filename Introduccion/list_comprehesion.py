my_original_list = [1, 2, 3, 4, 5]

my_list = [i for i in my_original_list]
print(my_list)

# crea lista numerica
# cada elemento del for agreguelo como elemento de una lista
my_list2 = [i for i in range(8)]
print(my_list2)

my_range = range(8)
print(my_range)

my_list_range = list(my_range)
print(my_list_range)

# Operacion pre-creacion de la lista
def sum_five(number):
    return number + 5

my_list2 = [sum_five(i) + 1 for i in range(8)]
print(my_list2)