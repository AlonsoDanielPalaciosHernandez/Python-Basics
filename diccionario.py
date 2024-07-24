my_dict= {}
print(type(my_dict))

other_dict = {
    "Nombre:":"Alonso", 
    "Apellido":"Palacios", 
    "Edad":26, 
    "Lenguajes":["Python","Swift","Kotlin"]
    }
my_dict = {"Nombre:":"Alonso", "Apellido":"Palacios", "Edad":26, 1:"Python"}
print(my_dict)
print(other_dict)
print(my_dict["Apellido"])
print(other_dict["Lenguajes"]["Python"])