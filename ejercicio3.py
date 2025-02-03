nombre = input("¿Cuál es tu nombre? ")
producto1 = float(input("Ingresa el precio de tu primer producto: "))
producto2 = float(input("Ingresa el precio de tu segundo producto: "))
producto3 = float(input("Ingresa el precio de tu tercer producto: "))
dinero = float(input("¿De qué valor es tu billete? "))
cambio = dinero - producto1 - producto2 - producto3
print("Tu cambio es de: ",cambio)