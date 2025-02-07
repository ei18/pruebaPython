## EJERCICIO 1:
# Supón que tienes un diccionario con los nombres de algunos estudiantes y sus respectivas calificaciones en una materia. Tu tarea es crear un diccionario nuevo que contenga los nombres de los estudiantes y sus calificaciones aumentadas enn un 10 %
# OBJETIVO: Crear un nuevo diccionario con las calificaciones aumentadas en un 10 %, pero sin usar ciclos (for) ni condicionales (if).
# PISTAS: Puedes hacer uso de map() para aplicar una operación a cada valor en el diccionario y luego combinar

estudiantes = {"Keity":99,
               "Juliana":97,
               "Dania:":80,
               "Alejandra":78
               }

calificaciones = dict(zip(estudiantes.keys(), map(lambda x: x * 1.10, estudiantes.values())))

print(calificaciones)

## EJERCICIO 2:
# Tienes un diccionario con los nombres de algunas ciudades y sus respectivas temperaturas en grados Celsius. Tu tarea es crear un diccionario nuevo con los nombres de las ciudades y sus temperaturas convertidas a grados Fahrenheit. No utilizar ni ciclos ni condicionales

ciudades = {"París": 18,
            "Madrid": 25,
            "Nueva York": 22,
            "Oslo": 20
            }

temperaturaFahrenheit = {ciudad: (temp * 9/5) + 32 for ciudad, temp in ciudades.items()}

print(temperaturaFahrenheit)
