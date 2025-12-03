# ------------------------------------------------------------
# Fibonacci Series with Python ;)
# Nombre: Navarro Hernández Dylan Alexander
# Matrícula: 2530220
# Grupo: IM-1:1
# ------------------------------------------------------------
"""
RESUMEN EJECUTIVO
La serie de Fibonacci es una secuencia de números donde cada término se obtiene sumando los dos anteriores, 
comenzando normalmente con 0 y 1. Calcular la serie hasta un número de términos n significa generar 
los primeros n valores siguiendo esa regla. Este programa realiza la lectura del valor n, valida que sea un 
entero permitido y, si es correcto, genera y muestra la serie de Fibonacci hasta completar la cantidad de 
términos solicitados.
"""
"""
DESCRIPCION:
El programa genera una serie de Fibonacci utilizando un ciclo while.
La serie comienza en 0 y 1, y va agregando cada término a una cadena 'generator'
separada por comas. El usuario ingresa la cantidad de términos n, y el programa
produce n+1 términos debido a la condición del contador (counter <= n).

Entradas:
- n (int; valor ingresado por el usuario indicando cuántos términos generar).

Salidas:
- generator: cadena con los términos de Fibonacci separados por comas.
  Ejemplo: "0,1,1,2,3,5,".

Validaciones:
- n debe convertirse correctamente a entero.
- n debe cumplir 0 <= n <= 50.
- Si n no cumple la validación, se muestra: "Error: invalid input".
- Si la conversión a entero falla, se muestra: "Error. only integers are allowed".

Casos de prueba:
1) Normal:
   Input: n = 5
   Output: "0,1,1,2,3,5,"

2) Borde:
   Input: n = 0
   Output: "0,"

3) Error:
   Input: n = "abc"
   Output: "Error. only integers are allowed"
"""


print("Welcome to fibonacci series generator")
n = input("Enter the number of terms:")
try: 
    n = int(n)
    first_number = 0
    second_number = 1
    next_number = 0
    generator = ""
    if n <= 50 and n >= 0:
        while counter <= n:  
            generator += str(first_number) + ","
            next_number = first_number + second_number
            first_number = second_number
            second_number = next_number
            counter += 1
        print(generator)
    else: 
        print("Error: invalid input")
except:
    print("Error. only integers are allowed") 

"""
CONCLUSIONES
El uso de un bucle facilitó generar la serie de Fibonacci de manera ordenada y repetitiva sin escribir código redundante. 
También fue importante manejar correctamente los casos n = 1 y n = 2, pues requieren imprimir solo los primeros valores sin cálculos adicionales. 
Además, la lógica implementada puede reutilizarse en otros programas donde se necesiten secuencias numéricas, acumulaciones progresivas 
o generación de patrones basados en términos anteriores.

REFERENCIAS
1) Python Documentation – While and For Loops
2) W3Schools – Python Fibonacci Examples
3) Real Python – Working with Loops and Sequences
"""
#Repositorio de github
"""
https://github.com/dNavarro-07/homework_projects
"""