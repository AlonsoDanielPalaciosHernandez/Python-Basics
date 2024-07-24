#Los set no son una estructura ordenada
#No aplica repetidosa y no podemos acceder a los elementos
my_set = set()
other_set = set()

print(type(my_set)) 

my_set={"Alonso","Palacios",26}

other_set={"Karen","Martinez",24}
print(my_set)
print(type(my_set)) 

#print(len(my_set[0]))

my_set.add("Hernandez")
print(my_set)

my_set.add("Alonso")
print(my_set)

print("Alonso" in my_set)
print("Alonsito" in  my_set)

my_set.discard("Hernandez")
print(my_set)

new_set = my_set.union(other_set)
print(new_set)

print(new_set.difference(other_set))
