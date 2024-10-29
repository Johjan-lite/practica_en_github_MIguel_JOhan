from math import sqrt
x=int(input ("INtroduce el primer numero: "))
y=int(input ("Introduce el segundo numero: "))
print (f"El resultado de la suma {x} y {y} es igual a {x+y}")
print ("""1: Elevar el primer numero por el segundo
       2: multiplicar el primer numero por el segundo
       3: Si es 3, obtener el promedio de la sumatoria de los numeros.
       4: Sumar los dos numeros
       5: Sumar ambos numeros y calcular su raiz cuadrada.""")
z=int(input("Ingrese un numero entero del 1 al 5: "))
while z>5 or z<1:
    print("Ese no es un numero valido")
    z=int(input("Ingrese un numero entero del 1 al 5: "))
if z==1:
    print (f"el resultado de {x}elevado a {y} es {x**y}")
elif z==2:
    print(f"El resultado de la multiplicación entre {x} y {y} es {x*y}")
elif z==3: 
    print (f"el promedio de la sumatoria entre {x} y {y} es {(x+y)/2}")
elif z==4: 
    print (f"El resultado de la suma entre {x} y {y} es igual a {x+y}")
elif z==5:
    print (f"La raiz cuadrada de la suma entre {x} y {y} es igual a {sqrt(x+y)}")


