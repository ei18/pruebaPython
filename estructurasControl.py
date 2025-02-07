## CONDICIONALES if - elif -else
# Identación

""" 
edad = 16
if edad >= 18:
    print("Mayor de edad")
    print("Se le puede vender cerveza")
else:
    print("Es menor de edad")    
    print("No le vendo nada")
print("Por aquí continúa el flujo")    
"""

edad = int(input("Ingrese la edad: "))

if edad >= 0 and edad < 6:
    print("Primera infancia")
elif edad >= 6 and edad < 13:
    print("Niñez")  
elif edad >= 13 and edad < 18:
    print("Adolescente")      
else:
    print("Adulto")    

## EJERCICIO 1:
# Supón que tienes un diccionario con las edades de varias personas. Tu tarea es crear un nuevo diccionario que indique si cada persona es mayor de edad o menor de edad.
# Las edades de referencia son: Mayor de edad: 18 años o más. Menor de edad: Menos de 18 años.
# OBJETIVO: crear un nuevo diccionario en el que las claves sean los nombres de las personas y los valores sean "Mayor de edad" o "Menor de edad" según corresponda.

personas = {"Luna": 16,
            "Celeste": 13,
            "Pablo": 10,
            "Valentina": 25
            }    

## EJERCICIO 2:
# Supón que tienes un diccionario con los resultados de varios exámenes de estudiantes. Tu tarea es crear un nuevo diccionario que contenga los nombres de los estudiantes y su respectivo estado en función de su calificación.
# Las reglas son: Si la calificación es 6 o mayor, el estado es "Aprobado". Si la calificación es menor a 6, el estado es "Reprobado"

resultados = {"María": 8,
              "Juan": 7,
              "José": 5,
              "Martha": 6
              }
