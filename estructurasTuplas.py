## TUPLAS ()

""" 
lista = [5, 68, "Hola"]
tupla = (5, 68, "Hola")
"""

#tuple() método constructor
frutas = tuple(("fresa", "manzana", "papaya", "manzana"))
print(frutas)

## Forma fácil
frutas2 = ("fresa", "manzana", "papaya", "manzana")
print(frutas2)

print(frutas.count("manzana")) ## .count() Cuenta
print(frutas.index("manzana")) ## .index() Encuentra la posición del elemento, si está repetida solo cuenta la primera posición 

## Hacer casteo con Lista, de esta manera ya se pueden utilizar otros métodos y cuando ya se hagan los cambios se vuelve a cambiar a Tupla
temporal = list(frutas)
print(temporal)
temporal.append("mango")
print(temporal)
frutas = tuple(temporal)
print(frutas)
print(frutas[2])

