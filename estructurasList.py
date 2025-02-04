## LISTAS
""" 
edad = 52
lista1 = ["Hola", 58, True, 3.1416]
print(len(lista1))

frutas = ["papaya", "fresa", "mango"]
print(frutas)
print(frutas[1])
"""

"""
frutas = ["papaya", "fresa", "mango"]
print(frutas)
frutas.append("naranja") ## Agregar elemento al final
print(frutas)
frutas.insert(2, "uva") ## Agrega elemento en la posición que yo elija
print(frutas)
frutas[2] = "mandarina" ## Reemplaza el elemento
print(frutas)
verduras = ["espinaca", "tomate", "lechuga"]
frutas.extend(verduras) ## Extiende la lista colocándole al final la otra lista que se creo
print(frutas)
## frutas.clear() ## Elimina los elementos dejando la lista vacía 
print(frutas)
## del frutas ## Elimina la lista
copia = frutas.copy() ## Hace una copia 
print(copia)
copia.append("perro")
print(copia)
print(frutas)
""" 

"""
verduras = ["espinaca", "tomate", "lechuga", "tomate"]
print(verduras.count("tomate")) ## .count cuenta los elementos
print(verduras.index("lechuga")) ## Devuelve la posición del elemento, si hay dos elementos iguales devuelve solo la posición del primero
verduras.pop() ## Elimina el último elemento 
print(verduras)
verduras.pop(1) ## Elimina el elemento de ese índice
print(verduras)
verduras.remove("lechuga") ## Remueve el elemento, si hay repetidos elimina solo el primero
print(verduras)
"""

verduras = ["espinaca", "tomate", "lechuga", "tomate"]
verduras.reverse() ## Reversa la lista. cambiando el orden del último al primero
print(verduras)
verduras.sort() ## Ordena en orden alfabético, para este método todos los elementos deben ser del mismo tipo
print(verduras)
