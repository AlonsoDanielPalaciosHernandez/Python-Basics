### funciones ###

def my_function ():
    print("Esto es una funcion")
    
my_function ()
my_function ()

##los elementos dentro de los parentesis() se les llama argumento o parametros
def sum_two_values(first_value,second_value):
    print(first_value + second_value)
    
sum_two_values(5,7)
sum_two_values(5.65,7.12)

#return
#Regresa valores pero no los imprime
def sum_two_values_with_return(first_value,second_value):
   return first_value + second_value
sum_two_values_with_return(11, 20)
my_result = sum_two_values_with_return(11, 20)
print(my_result)# solo se imprime si lo  mandamos a imprimir

def print_name(name, surname):
    print(f"mi nombre es {name} y mi segundo nombre es {surname}")
    
print_name("Alonso","Daniel")
print_name(surname="Michelle", name="Karen")#Le podemos dar orden definiendolos

#Funcion con valores por default
def print_name_with_default(name, surname = "----", nickname ='"Sin alias"'):#En nickname le puedo dar valor por defecto
    print(f"mi nombre es {name} ,mi segundo nombre es {surname} y mi alias es {nickname}")
    
print_name_with_default("Alonso")

#con esto puedo meter varios parametros o argumentos
def print_text(*text):
    print(text)
print_text("Hola","como","estas")

#con esto puedo meter varios parametros, imprimirlos e incluso imprimirlos como quiera,
# en este caso queria que los parametros se hicieran mayusculas
def print_texts_for(*texts):
    for text in texts:
        print(text.upper())
        print(text.capitalize())
        
print_texts_for("jitomates","cebolla","lechuga","queso")
