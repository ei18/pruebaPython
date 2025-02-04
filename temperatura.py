## Ask the user the temperture and print if it's cold, warm or hot.

temp = int(input("¿Cuál es la temperatura en este momento? "))

if temp < 15:
  print("Está frío el clima")
elif temp < 25:
  print("Está tibio")
elif temp < 50:
  print("Está caliente")
else:
  print("¿Está seguro que esa es la temperatura?")