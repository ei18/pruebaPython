## Ask the user numbers A and B, and print the multiplication table of A up to B.

A = int(input("Ingrese un número para mostrar su tabla de multiplicación: "))
B = int(input("Ingrese el límite de la tabla: "))
i = 1
mult = A * 1
while mult <= B:
  print("Mult:",mult, "i:", i)
  i = i + 1
  mult = A * i