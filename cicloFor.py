# n = int(input("Ingrese un número: "))
# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)

frutas = ["manzana", "naranja", "pera", "papaya"]
for x in frutas: # x es una variable
    print(x)
print("Por aquí sigue el flujo")    

## EJERCICIO DE RECOPILACIÓN
# Pedir a 10 usuarios que ingresen nombre, apellido y edad. En una lista ubicar los menores de edad y en otra lista los mayores de edad.
# diccionario = {"nombre":"Keity", "cedula":"1017249128"}
# lista = []
# lista.append(diccionario)
# print(lista)

usuariosMayores = []
usuariosMenores = []

for i in range(10):
    print(f"Ingresando datos del usuario {i + 1}:")
    nombre = input("Ingresa tu nombre: ")
    apellido = input("Ingresa tu apellido: ")
    edad = int(input("Edad: "))

    usuario = {"nombre":nombre,
               "apellido":apellido,
               "edad":edad
               }
    
    if edad >= 18:
        usuariosMayores.append(usuario)
    else:
        usuariosMenores.append(usuario)  

print("Usuarios mayores de edad:")   
for usuario in usuariosMayores:
    print(f"{usuario["nombre"]} {usuario["apellido"]} - {usuario["edad"]} años")  

print("Usuarios menores de edad:")  
for usuario in usuariosMenores:
    print(f"{usuario["nombre"]} {usuario["apellido"]} - {usuario["edad"]} años")  