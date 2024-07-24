#bucle while
my_condition = 0
while my_condition < 10:
    print(my_condition)
    my_condition += 2

else: # else es opcional
    print("my condition its the same as 101")
    
    
while my_condition < 20:
    my_condition +=1
    if my_condition == 15:
        print ("Se detiene la ejecucion")
    elif my_condition == 14:
        break #break detiene la ejecucion 
    print(my_condition)

print("la ejecucion continua")

# Bucle For
# se va a ejecutar segun elementos tengamos en las lista, tuplas, sets o diccionarios

my_list = [10 , 15 , 20 ,43 , 12 , 2]

for element in my_list:
  print(element)
  
my_tuple = (26, 1.80, "Daniel", "Hernandez")
for element in my_tuple:
  print(element)
  
my_set = {"Alonso","Palacios",26}
for element in my_set:
    print(element)
    
my_dict = {
    "Nombre:":"Alonso", 
    "Apellido":"Palacios", 
    "Edad":26, 
    "Lenguajes":["Python","Swift","Kotlin"],
    1:"Egresado"
    }
#Esto solo imprimira los is
for element in my_dict:
    print(element)
    
#una manera de imprimir solo los valores
""" my_dict = my_dict.values()
for element in my_dict:
    print(element) """
#segunda forma de imprimir solo los valores
for element in my_dict.values():
    print(element)
    if element == 26:
      print("Aqui finalizo")
      break
else:
    print("el bucle for para diccionario a finalizado")
    
for element in my_dict.values():
    print(element)
    if element == 26:
      continue # Realiza un especie de break, deteniendo la ejecucion en ese punto
               # y regresando al inicio del for
    print("continua y se ejecuta")
else:
    print("el bucle for para diccionario a finalizado")