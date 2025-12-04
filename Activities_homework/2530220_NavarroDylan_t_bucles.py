# ------------------------------------------------------------
# Manejo de bucles en Python
# Nombre: Navarro Hernández Dylan Alexander
# Matrícula: 2530220
# Grupo: IM-1:1
# ------------------------------------------------------------
#RESUMEN EJECUTIVO
"""
Un bucle for se utiliza para repetir instrucciones un número conocido de veces, normalmente recorriendo secuencias como rangos, listas o cadenas. 
En cambio, un bucle while ejecuta código mientras se cumpla una condición lógica, por lo que es más natural usarlo cuando no sabes cuántas iteraciones habrá. 
Un contador es una variable que aumenta paso a paso para llevar registro del número de repeticiones, mientras que un acumulador suma valores durante el proceso. 
Es fundamental definir bien la condición de salida de los bucles para evitar ciclos infinitos y errores lógicos. 
Este documento cubrirá la descripción de cada problema, el diseño de entradas y salidas, las validaciones necesarias y el uso adecuado de for y while 
en diferentes situaciones como recorridos, menús y lectura repetida de datos.
"""
#PRINCIPIOS Y BUENAS PRÁCTICAS
"""
- Usar for cuando se conoce de antemano cuántas iteraciones necesitas (por ejemplo, recorrer un rango de 1 a 10).
- Usar while cuando las repeticiones dependen de una condición (por ejemplo, esperar a que el usuario escriba "EXIT").
- Inicializar contadores y acumuladores antes de entrar al bucle.
- Actualizar las variables de control dentro del while para evitar ciclos infinitos.
- Mantener el cuerpo del bucle simple y, si es necesario, mover lógica compleja a funciones separadas.
"""
print("---------------------------------------------------------------------")
print("------------------(Problem 1: Sum of range with for)-----------------")
#Problem 1: Sum of range with for
"""
Descripción:
Este programa recibe un número entero n y calcula la suma de todos los números
desde 0 hasta n (incluido). También calcula por separado la suma de los números
pares dentro del mismo rango. Ambos cálculos se realizan usando un ciclo for.

Entradas:
- n (int): límite superior del rango.

Salidas:
- sum 1...n: suma total desde 0 hasta n.
- Even sum 1...n: suma de los números pares dentro del rango.

Validaciones:
- Solo se permiten enteros.
- Si el valor no puede convertirse a entero, se muestra:
  "Error. Only integers are allowed".
- El programa no valida si n es negativo; simplemente calcula desde 0 hasta n.

Casos de prueba:
1) Normal:
   Input: n = 10
   Output: sum 1...n: 55 | even sum: 30

2) Borde:
   Input: n = 0
   Output: sum 1...n: 0 | even sum: 0

3) Error:
   Input: n = "abc"
   Output: "Error. Only integers are allowed"
--------------------------------------------------------------
"""

n = input("Enter a number: ").strip()

try: 
    n = int(n)
    total_sum = 0
    even_sum = 0
    for number in range (n + 1):
        total_sum += number

        if number % 2 == 0:
            even_sum += number 
        
    print(f"sum 1...n: {total_sum}")
    print(f"Even sum 1...n : {even_sum}")

except:
    print("Error. Only integers are allowed")

print("---------------------------------------------------------------------")
print("--------------(Problem 2: Multiplication table with for)-------------")
#Problem 2: Multiplication table with for
"""
Descripción:
El programa recibe una base y un límite m, ambos enteros, y genera una tabla
de multiplicar desde 1 hasta m. En cada línea se muestra el producto de la base
por el contador actual.

Entradas:
- base (int): número base de la tabla.
- m (int): límite superior del rango de multiplicaciones.

Salidas:
- Una línea por multiplicación con el formato:
  "<m> x <contador> = <resultado>"

Validaciones:
- base y m deben ser convertibles a enteros.
- Si ocurre un error en la conversión, se muestra:
  "Error. Invalid input".
- El programa no valida si m es negativo; simplemente ejecuta range(1, m+1).

Casos de prueba:
1) Normal:
   Input: base=5, m=4
   Output: 4 x 1 = 5 ... 4 x 4 = 20

2) Borde:
   Input: base=7, m=1
   Output: "1 x 1 = 7"

3) Error:
   Input: base="hola", m=5
   Output: "Error. Invalid input"
--------------------------------------------------------------
"""

base = input("Insert the base of the multiplication: ").strip()
m = input("The limit of the multiplication: ").strip()

try:
    base = int(base)
    m = int(m)
    multiplications = 0
    max = 0
    for limit in range(1, m + 1):
        max += 1

        results = base * limit
        print (f"{m} x {max} = {results}")
except:
    print("Error. Invalid input")

print("---------------------------------------------------------------------")
print("-----(Problem 3: Average of numbers with while and sentinel)---------")
#Average of numbers with while and sentinel
"""
Descripción:
Este programa lee números enteros de forma repetida hasta que el usuario
ingrese el valor sentinela -1. Suma todos los valores válidos y calcula el
promedio al final. También cuenta cuántos números fueron ingresados antes
del sentinela.

Entradas:
- number (int): valor ingresado en cada iteración.
- SENTINEL_VALUE = -1

Salidas:
- count: cantidad de números válidos ingresados.
- average: promedio de los números.
- Si no se ingresan números válidos:
  "Error. No data"

Validaciones:
- Cada entrada debe convertirse a entero.
- Si la conversión falla, se muestra:
  "Error: Invalid input"
  y se pide otro número.
- El sentinela -1 no se incluye en los cálculos.

Casos de prueba:
1) Normal:
   Input: 5, 10, -1   (No cuenta -1)
   Output: count=2 | average=7.5

2) Borde:
   Input: -1 (primer valor)
   Output: "Error. No data"

3) Error:
   Input: "abc", 8, -1
   Output: muestra error y luego procesa 8 correctamente
--------------------------------------------------------------
"""
number = None
SENTINEL_VALUE = -1
count = 0
acumulator = 0
while number != SENTINEL_VALUE:
    number = input("Enter a number (-1 to finish): ").strip()
        
    try:
        number = int(number) 
        if not number == SENTINEL_VALUE:       
            acumulator += number
            count += 1
        
    except: 
        print("Error: Invalid input")
        continue

if count == 0:
    print("Error. No data")
else:
    average_value = acumulator / count

    print(f"count: {count}")
    print(f"average: {average_value}")

print("---------------------------------------------------------------------")
print("--------------(Problem 4: Password attempts with while)--------------")
#Problem 4: Password attempts with while
"""
Descripción:
El programa solicita al usuario escribir una contraseña. Tiene hasta cinco
intentos (MAX_ATTEMPS = 5). Si ingresa correctamente "Admin123", el programa
muestra "Login success". Si falla todos los intentos, muestra "Account locked".

Entradas:
- user_password (string): contraseña escrita por el usuario.

Salidas:
- "Login success" si la contraseña es correcta.
- "Account locked" si el usuario falla los 5 intentos.

Validaciones:
- La verificación es sensible a mayúsculas y minúsculas.
- Se cuentan correctamente los intentos.
- MAX_ATTEMPS = 5 está definido dentro del programa.

Casos de prueba:
1) Normal:
   Input: *falla una vez, luego escribe "Admin123"*
   Output: "Login success"

2) Borde:
   Input: *acierta en el quinto intento*
   Output: "Login success"

3) Error:
   Input: *cinco contraseñas incorrectas*
   Output: "Account locked"
--------------------------------------------------------------
"""
attemps = 0
MAX_ATTEMPS = 5
PASSWORD = "Admin123"
while attemps !=  MAX_ATTEMPS:
    user_password = input("Enter the password: ").strip()

    if user_password == PASSWORD:
        print("Login success")
        break
    else: 
        attemps += 1
if attemps == MAX_ATTEMPS:
    print("Account locked")

print("---------------------------------------------------------------------")
print("----------------(Problem 5: Simple menu with while)------------------")
#Problem 5: Simple menu with while
"""
Descripción:
Este programa muestra un menú interactivo que se repite hasta que el usuario
ingresa la opción 0. Permite saludar, mostrar el valor de un contador e
incrementarlo.

Entradas:
- option (int): opción del menú elegida por el usuario.

Salidas:
- "Hello!" (opción 1)
- "Counter: <valor>" (opción 2)
- "Counter incremented" (opción 3)
- "Bye!" (opción 0)
- "Error: invalid option" para opciones inválidas.

Validaciones:
- Se intenta convertir la entrada a int.
- Si falla, muestra "Error: invalid option" y vuelve a pedir.
- Solo se aceptan opciones 0,1,2,3.

Casos de prueba:
1) Normal:
   Input: 1
   Output: "Hello!"

2) Borde:
   Input: 0 inmediatamente
   Output: "Bye!"

3) Error:
   Input: "hola"
   Output: "Error: invalid option"
--------------------------------------------------------------
"""
option = None
counter = 0

while option != 0:
    print("1) Show greeting")
    print("2) Show current counter value")
    print("3) Increment counter")
    print("0) Exit")

    choice = input("Choose an option: ").strip()

    try:
        option = int(choice)
    except:
        print("Error: invalid option")
        continue

    if option == 1:
        print("Hello!")

    elif option == 2:
        print("Counter:", counter)

    elif option == 3:
        counter += 1
        print("Counter incremented")

    elif option == 0:
        print("Bye!")
    
    else:
        print("Error: invalid option")

print("---------------------------------------------------------------------")
print("---------(Problem 6: Pattern printing with nested loops)-------------")
#Problem 6: Pattern printing with nested loops
"""
Descripción:
Este programa imprime un patrón de asteriscos en forma de triángulo creciente
y luego decreciente. Primero imprime desde 1 a n asteriscos, y después vuelve
a descender hasta 1.

Entradas:
- n (int): número de filas del patrón.

Salidas:
- Patrón de incremento:
  *
  **
  ***
- Patrón de descenso:
  **
  *

Validaciones:
- n debe convertirse a número entero.
- Si la conversión falla:
  "Error. Invalid input"

Casos de prueba:
1) Normal:
   Input: n=4
   Output: *
           **
           ***
           ****
           ***
           **
           *

2) Borde:
   Input: n=1
   Output: "*"

3) Error:
   Input: "abc"
   Output: "Error. Invalid input"
--------------------------------------------------------------
"""
n = input("Enter the number of rows:").strip()
row = "*"
acumulator = 0
try:
    n = int(n)

    for rows in range(1,n+1):
        acumulator += 1 
        row = "*" *(acumulator)
        print(row)

    for rows in range(0,n-1):
        acumulator -= 1 
        row = "*" *(acumulator)
        print(row)
except:
    print("Error. Invalid input")
#CONCLUSIONES
"""
El uso de for y while tiene diferencias prácticas importantes: for es ideal cuando conocemos el número de repeticiones, mientras que while funciona mejor cuando dependemos de una condición variable. 
Los contadores y acumuladores fueron esenciales para controlar iteraciones y realizar cálculos progresivos dentro de los bucles. 
Al trabajar con while, comprendí los riesgos de generar ciclos infinitos si no se actualizan correctamente las variables de control. 
También observé que los menús interactivos y los sistemas de intentos de contraseña son aplicaciones muy naturales del bucle while. 
Finalmente, aprendí cómo funcionan los bucles anidados y cómo permiten generar patrones repetitivos o estructuras más complejas dentro del programa.
"""
#REFERENCIAS
"""
1) Python documentation – for statements, while statements  
2) W3Schools – Python Loops (for, while)  
3) Real Python – Looping Techniques in Python  
4) Automate the Boring Stuff with Python – Chapter on Flow Control  
5) Programiz – Python Loops Explained  
"""
##Repositorio de github
"""
https://github.com/dNavarro-07/homework_projects.git
"""

