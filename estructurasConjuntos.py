## CONJUNTOS {}

""" 
conjunto = {"carro", "casa", "beca", "empresa"}
conjunto2 = set(("carro", "casa", "beca", "empresa")) # set -> conjunto
print(conjunto)
print(conjunto2)
"""

frutas = {"manzana", "piña", "naranja", "mandarina", "Ferrary"}
carros = {"Toyota", "Fiat", "Ferrary", "Fiat", "piña"}
verduras = {"piña", "guayaba"}
print(frutas)
print(carros)

## Métodos
frutas.add("guanábana") # .add() Agrega elementos
print(frutas)
# frutas.clear() # .clear() Limpia
# del frutas # del Elimina todo
copia = frutas.copy() # .copy() Crea una copia
print(copia)
print(frutas.difference(carros)) # .difference 
frutas.discard("guanábana") # .dicard Saca un elemento que ya existe 
print(frutas)
# frutas.discard("piña")
# frutas.remove("kiwi") # .remove() Hace lo mismo, pero con la diferencia que si no está saca un error
# print(frutas.pop()) # .pop() Saca un elemento aleatorio 
print(frutas.intersection(carros)) # .intersection() Devuelve un conjunto con los elementos que están en ambos
print(frutas.intersection(carros.intersection(verduras))) # varios conjuntos
 
# Todos los elementos del pequeño quedan en el grande. Si es subconjunto del conjunto 1. devuelve True
conjunto1 = {1, 2, 3, 4, 5, 6}
conjunto2 = {3, 5}
print(conjunto2.issubset(conjunto1))
print(conjunto1.issuperset(conjunto2)) # Están abarcados