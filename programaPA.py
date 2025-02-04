## Haga un programa que le pida al usuaio las medidas de presión arterial de un paciente y luego le diga cuál fue la más alta.

datos = []
pa = 0
while pa != "x":
 pa = input("Ingrese la presión arterial: ")
 datos.append(pa)
 print(datos)

# Esta parte del código es para encontrar el máximo
datos.pop()
print(datos)

i = 0
maximo = 0
while i < len(datos):
  #length: longitud
  if int(datos[i]) < 100:
    print("Tienes bajita la presión")
  elif int(datos[i]) < 200:
    print("Tienes la presión normal")
  else:
    print("Tienes la presión alta")

  if int(datos[i]) > maximo:
    maximo = int(datos[i])
  i = i + 1

print(maximo)
print("Fin")
