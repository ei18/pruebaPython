# Devuelven o no valores
# Reciben o no valores
# Reutilizar código

def funcion1(): # No se ejecuta hasta que no se llame. NO recibe datos
    print("Hola") 

def suma(a, b): # Recibe datos en 2 variables --> parámetros. NO devuelve valores
    print("El resultado es: ", a+b)

def suma2(a, b): # SÍ devuelve valores
    resultado = a + b
    return resultado

def ensayo():
    a = 5 # La variable solamente vive dentro de la función. 
    print(a)
    print(saludo) # Si se define una variable afuera sí vive en todas partes a donde se llame

def ensayo2(*a):
    print(a)    

def ensayo3(a, b):
    print(a+b)
    print(a)
    print(b)

funcion1()    # Siempre () así no se le pase nada
suma(5, 3) # Si se le pasan 2 parámetros, debe recibir 2 también. NO devuelve 
print(suma2(5, 3)) # Se convierte en lo que devuelve, para mostrarlo es con print()

saludo = "Hola" # Si se define una variable afuera sí vive en todas partes a donde se llame. La variable se debe llamar primero antes que la función
ensayo()

ensayo2(8, 9, 6, 3, 5, 7, 6)
ensayo3(b=18, a=1)


