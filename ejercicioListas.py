## Cree un programa que pida nombres a un usuario y los almacene en una lista. El proceso se repite hasta que el usuario digite x. Al finalizar se deben listar los nombres ingresados y su posición.

usuarios = []

while True:
    nombre = input("Digite un nombre o x: ")

    if nombre == "x":
        break

    usuarios.append(nombre)

print("Usuarios registrados:", usuarios)    
