# ------------------------------------------------------------
# Fibonacci Series with Python ;)
# Nombre: Navarro Hernández Dylan Alexander
# Matrícula: 2530220
# Grupo: IM-1:1
# ------------------------------------------------------------
#RESUMEN EJECUTIVO
"""
Una función en Python es un bloque de código reutilizable diseñado para ejecutar una tarea específica, lo que permite organizar mejor los programas. 
Los parámetros son las variables que aparecen en la definición de la función, mientras que los argumentos son los valores reales que se envían al llamarla. 
Separar la lógica en funciones ayuda a reducir la repetición de código y facilita la lectura, el mantenimiento y las pruebas del programa. 
Un valor de retorno permite que la función entregue resultados para que otras partes del programa los usen, lo cual es más flexible que únicamente imprimirlos. 
Este documento incluirá la descripción de cada problema, el diseño de las funciones usadas, sus entradas y salidas, las validaciones aplicadas y pruebas básicas para verificar su correcto funcionamiento.
"""
#PRINCIPIOS Y BUENAS PRÁCTICAS
"""
- Usar funciones pequeñas que cumplan una sola tarea (single responsibility).
- Evitar repetir código: si un bloque se repite, convertirlo en una función.
- Preferir funciones “puras” cuando sea posible: mismo input → mismo output, sin depender de variables externas.
- Documentar cada función con comentarios claros sobre qué hace y qué parámetros recibe.
- Nombrar las funciones de manera descriptiva, por ejemplo calculate_total(), validate_input(), en lugar de nombres genéricos como func() o process().
"""

print("----------------------------------------------------------------------")
print("-----(Problem 1: Rectangle area and perimeter (basic functions))------")
#Problem 1: Rectangle area and perimeter (basic functions)
"""
Descripción:
El programa calcula el área y el perímetro de un rectángulo usando funciones
separadas. Primero intenta convertir los valores ingresados a números reales.
Si la conversión falla o si los valores son menores o iguales a cero, muestra
un mensaje de error. Si los valores son válidos, calcula el área y el perímetro.

Entradas:
- weidth (float): base del rectángulo.
- height (float): altura del rectángulo.

Salidas:
- Area calculada (weidth * height).
- Perimeter calculado (2*weidth + 2*height).

Validaciones:
- Ambos valores deben poder convertirse a float.
- Ambos valores deben ser mayores que cero.
- Si falla la conversión, automáticamente los valores se vuelven 0 y genera error.

Casos de prueba:
1) Normal:
   Input: weidth=5, height=3
   Output: Area: 15 | Perimeter: 16

2) Borde:
   Input: weidth=0, height=4
   Output: "Error. Invalid input"

3) Error:
   Input: weidth="abc", height="10"
   Output: "Error. Invalid input"
"""
def calculate_area(weidth, height):
        return weidth * height
def calculate_perimeter(weidth, height):
         return weidth * 2 + height * 2

weidth = input("Enter the weidth: ").strip()
height = input("Enter the height: ").strip()

try:
    weidth = float(weidth)
    height = float(height)
except:
      weidth = 0
      height = 0

if weidth <= 0 or height <=0:
    print("Error. Invalid input")
else:
    area_value = calculate_area(weidth, height)
    perimeter_value = calculate_perimeter(weidth, height)
    print(f"Area: {area_value}")
    print(f"Perimeter: {perimeter_value}")

print("----------------------------------------------------------------------")
print("-------------------(Problem 2: Grade classifier)----------------------")
#Problem 2: Grade classifier (function with return string)
"""
Descripción:
El programa clasifica una calificación numérica dentro de una categoría de letra
(A, B, C, D o F) usando la función classify_grade(score). Primero convierte el
input a número real. Si está fuera del rango 0–100 o la conversión falla,
muestra un mensaje de error.

Entradas:
- score (float): calificación entre 0 y 100.

Salidas:
- Score: valor ingresado.
- Category: A, B, C, D o F.

Validaciones:
- El valor debe convertirse a float.
- Debe estar entre 0 y 100.
- Cualquier valor fuera del rango produce error.
- Cualquier input no numérico produce error.

Casos de prueba:
1) Normal:
   Input: score=85
   Output: Score: 85 | Category: B

2) Borde:
   Input: score=100
   Output: Category: A

3) Error:
   Input: score="hola"
   Output: "Error: invalid input"
"""

def classify_grade(score):
   
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"
    
score = input("Enter score (0-100): ").strip()

try:
    score = float(score)

    if score < 0 or score > 100:
        print("Error: invalid input")
    else:
        grade = classify_grade(score)
        print(f"Score: {score}")
        print(f"Category: {grade}")

except:
    print("Error: invalid input")

print("----------------------------------------------------------------------")
print("-------------------(Problem 3: Grade classifier)----------------------")
#Problem 3: List statistics function (min, max, average)
"""
Descripción:
El programa recibe una lista de números separados por comas, los convierte a float
y calcula el mínimo, máximo y promedio usando la función summarize_numbers.
Si algún elemento no es numérico, si la cadena está vacía o si no hay números
válidos, muestra un mensaje de error.

Entradas:
- numbers_text (string): números separados por comas.
- numbers_list (list[float]): lista convertida a flotantes.

Salidas:
- Min: valor mínimo.
- Max: valor máximo.
- Average: promedio de los valores.

Validaciones:
- La cadena no puede estar vacía.
- Cada elemento debe poder convertirse a float.
- No se permiten listas vacías.
- Cualquier error en conversión produce "Error: invalid input".

Casos de prueba:
1) Normal:
   Input: "3, 5, 10"
   Output: Min=3 | Max=10 | Average=6

2) Borde:
   Input: "7"
   Output: Min=7 | Max=7 | Average=7

3) Error:
   Input: "3, , 5"
   Output: "Error: invalid input"
"""

def summarize_numbers(numbers_list):
    
    result = {
        "min": min(numbers_list),
        "max": max(numbers_list),
        "average": sum(numbers_list) / len(numbers_list)
    }
    return result

numbers_text = input("Enter numbers separated by commas: ").strip()

if numbers_text == "":
    print("Error: invalid input")
else:
    parts = numbers_text.split(",")
    numbers_list = []

    try:
        for element in parts:
            number = float(element.strip())
            numbers_list.append(number)
        if len(numbers_list) == 0:
            print("Error: invalid input")
        else:
            stats = summarize_numbers(numbers_list)
            print(f"Min: {stats['min']}")
            print(f"Max: {stats['max']}")
            print(f"Average: {stats['average']}")

    except:
        print("Error: invalid input")

print("----------------------------------------------------------------------")
print("---------(Problem 4: Apply discount list (pure function))-------------")
# Problem 4: Apply discount list (pure function)
"""
Descripción:
El programa aplica un descuento a una lista de precios usando la función
apply_discount. Convierte los precios a float, valida que cada precio sea mayor
que cero y que la tasa de descuento esté entre 0 y 1. Si hay un error, se
muestra "Error: invalid input".

Entradas:
- prices_list (list[float]): precios originales.
- discount_rate (float): tasa de descuento entre 0 y 1.

Salidas:
- Original prices: lista sin descuento.
- Discounted prices: lista con descuento aplicado.

Validaciones:
- La lista de precios no puede estar vacía.
- Cada precio debe ser convertible a float y mayor que 0.
- discount_rate debe ser float y estar entre 0 y 1.
- Cualquier falla en conversión genera error.

Casos de prueba:
1) Normal:
   Input: prices="100,200", discount_rate=0.2
   Output: [100,200] → [80,160]

2) Borde:
   Input: prices="50", discount_rate=1
   Output: discounted=[0]

3) Error:
   Input: prices="10,-5", discount_rate=0.3
   Output: "Error: invalid input"
"""
def apply_discount(prices_list, discount_rate):
    
    discounted = []
    for price in prices_list:
        new_price = price * (1 - discount_rate)
        discounted.append(new_price)
    
    return discounted

prices_text = input("Enter prices separated by commas: ").strip()
discount_rate_text = input("Enter discount rate (0–1): ").strip()

if prices_text == "":
    print("Error: invalid input")
else:
    try:
        parts = prices_text.split(",")
        prices_list = []

        for p in parts:
            value = float(p.strip())
            if value <= 0:
                raise ValueError  
            prices_list.append(value)


        if len(prices_list) == 0:
            print("Error: invalid input")
            exit()

        discount_rate = float(discount_rate_text)

        if discount_rate < 0 or discount_rate > 1:
            print("Error: invalid input")
            exit()


        discounted_prices = apply_discount(prices_list, discount_rate)

        print(f"Original prices: {prices_list}")
        print(f"Discounted prices: {discounted_prices}")
    except:
        print("Error: invalid input")

print("----------------------------------------------------------------------")
print("--------(Problem 5: Greeting function with default parameters)--------")
# Problem 5: Greeting function with default parameters
"""
Descripción:
El programa genera un saludo personalizado usando la función greet, que admite
un título opcional. El nombre debe ser válido (no vacío). Si el nombre está
vacío, se muestra "Error: invalid input".

Entradas:
- name (string): nombre del usuario.
- title (string, opcional): título como "Mr.", "Dr.", etc.

Salidas:
- Greeting: saludo generado, como "Hello, Dr. Smith!".

Validaciones:
- El nombre no puede estar vacío.
- El título puede estar vacío.
- Se eliminan espacios extras con strip().

Casos de prueba:
1) Normal:
   Input: name="Alice", title="Dr."
   Output: Hello, Dr. Alice!

2) Borde:
   Input: name=" Bob ", title=""
   Output: Hello, Bob!

3) Error:
   Input: name=""
   Output: "Error: invalid input"
"""
def greet(name, title=""):

    name = name.strip()
    title = title.strip()

    if title != "":
        full_name = title + " " + name
    else:
        full_name = name

    return f"Hello, {full_name}!"

name_text = input("Enter name: ")
title_text = input("Enter title (optional): ")

if name_text.strip() == "":
    print("Error: invalid input")
else:
    greeting_msg = greet(name=name_text, title=title_text)

    print("Greeting:", greeting_msg)

print("----------------------------------------------------------------------")
print("-------(Problem 6: Factorial function (iterative or recursive))-------")
# Problem 6: Factorial function (iterative or recursive)
"""
Descripción:
El programa calcula el factorial de un número entero entre 0 y 20 usando una
función iterativa. Primero valida que el valor ingresado sea un entero mediante
isdigit(), luego verifica que esté dentro del rango permitido. Si no cumple,
muestra "Error: invalid input".

Entradas:
- n (int): número entero entre 0 y 20.

Salidas:
- n: valor válido.
- Factorial: resultado de n!.

Validaciones:
- Solo se aceptan enteros (no negativos o decimales).
- Rango permitido: 0 ≤ n ≤ 20.
- Si el input contiene caracteres no numéricos o un signo negativo no válido,
  produce error.

Casos de prueba:
1) Normal:
   Input: n=5
   Output: Factorial=120

2) Borde:
   Input: n=0
   Output: Factorial=1

3) Error:
   Input: n=25
   Output: "Error: invalid input"
"""
def factorial(n):
   
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n_text = input("Enter n: ")

if not n_text.lstrip("-").isdigit():
    print("Error: invalid input")
else:
    n = int(n_text)

    if n < 0 or n > 20:
        print("Error: invalid input")
    else:
        fac = factorial(n)
        print("n:", n)
        print("Factorial:", fac)

#CONCLUSIONES
"""
Las funciones hicieron que el programa fuera más ordenado porque permitieron dividir el código en partes pequeñas y claras.
Devolver valores con return fue útil para reutilizar resultados sin depender solo de imprimirlos.
El uso de parámetros y valores por defecto hizo el código más flexible y evitó repetir instrucciones.
Encapsular cálculos y validaciones dentro de funciones me ayudó a mantener la lógica principal más limpia.
Comprendí mejor cómo la lógica principal coordina el programa mientras las funciones de apoyo realizan tareas específicas.
En general, trabajar con funciones facilitó la lectura, depuración y expansión del programa.
"""
#REFERENCIAS
"""
- Python Software Foundation. "Defining Functions." Documentación oficial.
- W3Schools. "Python Functions" – Tutorial introductorio.
- Automate the Boring Stuff with Python – Capítulo sobre funciones.
- Real Python. "Understanding Functions and Scope."
- Apuntes de clase / material oficial del curso de Programación.
"""

#Repositorio de github
"""
https://github.com/dNavarro-07/homework_projects
"""