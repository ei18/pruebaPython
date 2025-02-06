## Ejercicio:
# 1. Crea una lista con 5 números enteros.
# 2. Usa la función sorted() para obtener una lista ordenada de menor a mayor.
# 3. Usa la función sum() para obtener la suma de todos los elementos de la lista.
# 4. Usa la función min() para obtener el valor mínimo de la lista.
# 5. Usa la función max() para obtener el valor máximo de la lista.

numeros = list(map(int, input("Ingresa 5 números enteros: ").split()))

lista = sorted(numeros)

suma = sum(numeros)

minimo = min(numeros)

maximo = max(numeros)

print("Lista: ", numeros)
print("Lista ordenada: ", lista)
print("Suma total: ", suma)
print("Valor mínimo: ", minimo)
print("Valor máximo: ", maximo)


