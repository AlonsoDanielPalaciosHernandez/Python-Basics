#arreglo, listas o arrays#


my_other_list=[]

my_list = [12 , 13 , 14 , 15]

print(my_list)
print(len(my_list))

my_other_list=[35, 1.80 , "Alonso", "Palacios"]
print((my_other_list[::-1]))
print(my_other_list + my_list)

my_list.append(900)
print(my_list)

my_other_list.insert(1, "este es un insert")
print(my_other_list)


suma = [ 1 , 2 , 5 ,3 , 4]
suma2 = [ 1 , 2 , 3 , 4]

print(suma[0] + suma2[3])
##copiamos la lista

new_list = suma.copy()
print(new_list)
new_list.reverse()
print(new_list)

##ordena
new_list.sort()
print(new_list)

##Se pueden modificar las listas, pero las tuples no
new_list[1] = 10
print(new_list)

