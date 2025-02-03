##Condicionales: instrucciones que le permiten a un algoritmo o programa tomar decisiones.

nombre = input("¿Cuál es tu nombre? ")
apellido = input("¿Cuál es tu apellido? ")
edad = int(input("¿Cuál es tu edad? "))
nacimiento = input("¿En qué país naciste? ")

if nacimiento.lower() == "colombia":
  print("Eres colombiano")
else:
  print("Eres extranjero")

if edad < 60 and edad >= 18:
  print("Eres adulto")

if nacimiento.lower() == "colombia" or nacimiento.lower() == "argentina" and nacimiento.lower() == "ecuador":
    print("Eres suramericano")

if edad < 18:
  print("Eres menor de edad")

elif edad < 40:
  print("Eres adulto joven")

elif edad < 60:
  print("Eres adulto no tan viejo")

else:
  print("Eres de la tercera edad")

print("Hola ", nombre + " " + apellido, "tienes", edad, "años")