## DICCIONARIOS {clave:valor}

diccionario = {"nombre":"Juliana", 
               "apellido":"Ortega", 
               "edad":27, 
               "celular":"3218781319"}
print(len(diccionario)) ## Longitud
print(diccionario["nombre"]) ## Mostrar lo que hay en el campo nombre (clave)
print(diccionario)
# diccionario.clear() Limpia
copia = diccionario.copy() # Crear copia
print(diccionario)
print(copia)
copia["edad"] = 18
print(copia)
print(diccionario)
print(diccionario.get("edad")) # Devuelve el valor asociado a esa llave
print(diccionario.items()) # Devuelve los valores asociados a las llaves. Tuplas con {llave : valor}
print(diccionario.keys()) # Devuelve todas las llaves
print(diccionario.values()) # Devuelve los valores asociados 
# print(diccionario.pop("apellido")) # Devuelve el último si no se le dice nada, o saca el que se le diga. ELIMINA 
diccionario.popitem() # Saca el último elemento
print(diccionario)
diccionario.setdefault("canthijos",0) # Devuelve el valor asociado a la llave, pero si no devuelve lo que se agregue
print(diccionario)
diccionario.update({"salario":8000000}) # Actualiza enviándole una una clave : valor
print(diccionario)