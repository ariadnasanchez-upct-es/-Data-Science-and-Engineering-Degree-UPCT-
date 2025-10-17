print("Práctica 2")

print("Ejercicio 1. Calculadora básica.")

a=int(input("Introduce el primer número\n"))
b=int(input("Introduce el segundo número\n"))
suma=a+b
resta=a-b
mult=a*b
div=a/b
divEntera=a//b
resto=a%b

#vamos a mostras los resultados por pantalla
print("La suma de", a, "+", b, "=", suma)
print("La resta de", a, "-", b, "=", resta)
print("La multiplicación de", a, "x", b, "=", mult)
print("La división de", a, "/", b, "=", div)
print("La división entera de", a, "/", b, "=", divEntera)
print("El resto de la división de", a, "/", b, "=", resto)

print("Ejercicio 2. Calculadora básica 2.")

#importamos el módulo math, siempre en la peimera línea de la celda
import math
from xml.etree.ElementTree import PI
c=int(input("Introduce un número entero\n"))
x=math.sqrt(c) #raíz cuadrada
y=math.fabs(c) #valor absoluto
z=math.log10(c) #logarítmo en base 10

print("La raíz cuadrada de", c, "es", x)
print("El valor absoluto de", c, "es", y)
print("El logarítmo en base 10 de", c, "es", z)

print("Ejercicio 3. Conversor de ángulos a radianes.")

ang=float(input("Introduce un valor real\n"))
angRad = (ang*math.pi)/180
e=math.sin(angRad)
f=math.cos(angRad)
g=math.tan(angRad)

print("El seno en radianes es",e)
print("El coseno en radianes es",f)
print("La tangente en radianes es",g)

print("Ejercicio 4. Ecuación.")

a=int(input("Introduzca un número entero\n"))
b=int(input("Introduzca un número entero\n"))
c=int(input("Introduzca un número entero\n"))

𝑥1=(-b+(math.sqrt(b**2)-(4*a*c)))/(2*a)
𝑥2=(-b-(math.sqrt(b**2)-(4*a*c)))/(2*a)
print("La solución 1 de la ecuación de segundo grado es", x1)
print("La solución 2 de la ecuación de segundo grado es", x2)

print("Ejercicio 5. Texto.")

s="""Todas las islas, incluso las conocidas,
son desconocidas mientras
no desembarquemos en ellas."""

print(s)

print("Ejercicio 6. Intercambio circular de valores")

# Solicitar al usuario que ingrese tres valores enteros
a = int(input("Introduce el valor de a\n"))
b = int(input("Introduce el valor de b\n"))
c = int(input("Introduce el valor de c\n"))

# Realizar el intercambio circular
aux=b
b=a
a=c
c=aux

# Mostrar los valores después del intercambio
print("Valores después del intercambio", a, b, c)

# Solicitar al usuario que ingrese tres valores enteros
a = int(input("Introduce el valor de a\n"))
b = int(input("Introduce el valor de b\n"))
c = int(input("Introduce el valor de c\n"))
d = int(input("Introduce el valor de d\n"))
# Realizar el intercambio circular
aux=a
a=b
b=c
c=d
d=aux

# Mostrar los valores después del intercambio
print("Valores después del intercambio", a, b, c, d)

