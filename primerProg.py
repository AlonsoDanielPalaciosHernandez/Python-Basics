# hello world
"""
comentario de 
varias
lineas
"""
'''
comentarios 
varias lineas

#Esto es un comentario
a= 5
b= 6
c= a + b
d= c * b

String= "este es un string"
print(c)
print (type(String))
print(a,b,c,d,String)
print("este es el valor de C:", c)

nombre = input('cual es tu nombre:')

edad = input('cual es tu edad:')
 
print("tu nombre es:" + nombre)
print("tu edad es:" + edad + " años") '''

name, surname, age = "Alonso", "palacios", 26
print("Mi nombre es {} {} y mi edad es {}".format(name,surname,age))
print("Mi nombre es %s %s y mi edad es %s"%(name,surname,age))

nombre ="alonso"
##edad = 2##
print(nombre.capitalize())
print(nombre.upper())
print(nombre.lower())
print(nombre.count("o"))
print(nombre.isnumeric())
print(nombre[::-1])
print(nombre.startswith("al"))
inicial = input('con que iniciales comienza tu nombre: ')
edad= input('tu edad: ')

print(nombre.startswith(inicial))

print(float(edad))

num = int(input("Escribe un numero"))
print(num)