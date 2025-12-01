# ------------------------------------------------------------
# Manejo de números y booleanos en Python
# Nombre: Navarro Hernández Dylan Alexander
# Matrícula: 2530220
# Grupo: IM-1:1
# ------------------------------------------------------------
#Resumen Ejecutivo
"""
Los tipos int y float en Python representan números enteros y números con decimales,
respectivamente, y se utilizan dependiendo del tipo de dato que se necesita procesar.
Los valores booleanos (True y False) se generan normalmente mediante comparaciones,
como >, <, >= o ==, y sirven para tomar decisiones dentro del programa. Validar rangos
es fundamental para evitar errores como divisiones entre cero o valores imposibles
(en temperaturas, horas o alturas). Este documento describe cada uno de los problemas,
especificando entradas, salidas, validaciones aplicadas y el uso de int, float y booleanos
para controlar el flujo del programa y garantizar que los cálculos sean correctos.
"""

#Principios y buenas practicas
"""
- Utilizar tipos adecuados: int para valores contables y float para cantidades con decimales.
- Evitar repetir cálculos complejos guardando resultados intermedios en variables.
- Validar todos los datos antes de operarlos, por ejemplo, evitar números negativos o vacíos.
- Usar nombres de variables claros y mensajes comprensibles para el usuario.
- Documentar lo que significa cada bandera booleana y en qué condiciones resulta True o False.
"""
print("---------------------------------------------------------------------")
print("------------(Problema 1: Temperature converter and range flag)-------")
#Problem 1: Temperature converter and range flag
"""
Descripción:
Este programa recibe una temperatura en grados Celsius, valida que sea un
número real y realiza su conversión a Fahrenheit y Kelvin. Además, activa
una bandera booleana que indica si la temperatura es considerada alta
(30 °C o más).

Entradas:
- temp_c (float): temperatura en grados Celsius ingresada por el usuario.

Salidas:
- Temperatura en Fahrenheit.
- Temperatura en Kelvin.
- high_temperature: True si temp_c >= 30, False si no.

Validaciones:
- Solo se aceptan números reales.
- Se verifica que la temperatura convertida a Kelvin no sea negativa, ya que
  el valor mínimo posible es -273.15 °C.
- Si la conversión a Kelvin es inválida se muestra un mensaje de error.

Casos de prueba:
1) Normal:
   Input: 25
   Output: fahrenheit: 77.0 | kelvin: 298.15 | high_temperature: False

2) Borde:
   Input: -273.15
   Output: kelvin = 0 | high_temperature: False
3)Error:
    Input:-280.15
    Output: "This temperature is not possible, the minimum limit is -273.15 C°"

3) Error:
   Input: "abc"
   Output: "Only numbers are allowed"
--------------------------------------------------------------
"""
temp_c = input("Enter celsius degress(°C): ").strip()

try:
    temp_c= float(temp_c)
    temp_f = temp_c * 9 / 5 + 32 
    temp_k = temp_c + 273.15 
    is_high_temperature = (temp_c >= 30.0)

    if temp_k >= 0:
        print(f"fahrenheit: {temp_f}")
        print(f"Kelvin: {temp_k}")
        print(f"high temperature: {is_high_temperature}")
        
    else:
        print("This temperature is not possible, the minimum limit is -273.15 C°")
except:
    print("Only numbers are allowed")

print("---------------------------------------------------------------------")
print("-------------(Problema 2:  Work hours and overtime payment)----------")
#Problem 2: Work hours and overtime payment

"""
Descripción:
El programa calcula el pago total semanal de un trabajador tomando en cuenta
horas normales (máximo 40) y horas extra, las cuales se pagan al 150% del
sueldo por hora. También determina si el trabajador generó horas extra.

Entradas:
- hours_worked (float): horas trabajadas en la semana.
- hourly_rate (float): pago por hora.

Salidas:
- Regular pay: pago por horas normales.
- Overtime pay: pago por horas extra (si existen).
- Total pay: suma total.
- has_overtime: True si trabajó más de 40 horas.

Validaciones:
- Las horas trabajadas deben ser >= 0.
- El pago por hora debe ser mayor que 0.
- Solo se aceptan números reales.

Casos de prueba:
1) Normal:
   Input: hours_worked=45, hourly_rate=100
   Output: regular=4000 | overtime=750 | total=4750 | has_overtime=True

2) Borde:
   Input: hours_worked=40, hourly_rate=80
   Output: overtime=0 | total=3200 | has_overtime=False

3) Error: Input: hours_worked= 50, hourly_rate= 
    Output: "hourly rate and hours worked must be bigger than 0"

3.1) Error:
   Input: hours_worked="abc"
   Output: "Only numbers are allowed"
--------------------------------------------------------------
"""

hours_worked = input("Enter hours worked this week: ").strip()
hourly_rate = input("Enter the hourly rate: ").strip()

try:
    hourly_rate = float(hourly_rate)
    hours_worked = float(hours_worked)
    if hours_worked >= 0 and hourly_rate > 0: 
        normal_hours = min(hours_worked,40)
        overtime_hours = max(hours_worked-40,0) 

        has_overtime = (hours_worked > 40)

        regular_pay = hourly_rate * normal_hours
        overtime_pay = overtime_hours * hourly_rate * 1.5
        total_pay = regular_pay + overtime_pay
    
        print(f"Regular pay: {regular_pay}")
        print(f"Overtime pay: {overtime_pay}")
        print(f"Total pay: {total_pay}")
        print(f"has overtime: {has_overtime}")

    else: 
        print("hourly rate and hours worked must be bigger than 0")
except:
    print("Only numbers are allowed")

print("---------------------------------------------------------------------")
print("-----------(Problema 3: Discount eligibility with booleans)----------")
# Problem 3: Discount eligibility with booleans
"""
Descripción:
El programa determina si un cliente es elegible para un descuento del 10%,
dependiendo de tres condiciones:
- sea estudiante,
- sea adulto mayor (senior),
- y su compra sea de al menos $1000.

Entradas:
- purchase_total (float): total de compra.
- is_student_text (string): "YES" o "NO".
- is_senior (string): "YES" o "NO".

Salidas:
- final_total: total con o sin descuento aplicado.

Validaciones:
- Los campos no deben estar vacíos.
- purchase_total debe ser numérico.
- Las respuestas deben ser exactamente "YES" o "NO" (en cualquier mayúscula/minúscula).
- Se verifica que todos los datos hayan sido proporcionados.

Casos de prueba:
1) Normal:
   Input: total=1500, student=YES, senior=YES
   Output: final_total=1350

2) Borde:
   Input: total=1000, student=NO, senior=YES
   Output: final_total=1000

3) Error:
   Input: total = 1200, student="ye", senior="si"
   Output: "Error. Invalid input"
3.1) Error: 
   Input: total = abd, student = "YES", senior = "YES"
   Output: "Error: the purchase total only allow numbers"
3.2) Error:
    Input: total = 1600, student = "", senior = "NO"
    Output: "Error.Verify you fill in all the information"
--------------------------------------------------------------
"""

purchase_total = input("Enter the purchase total:").strip()
is_student_text = str(input("Are you student? (YES/NO):")).strip()
is_senior = str(input("Are you a senior?(YES/NO):")).strip()

discount_elegible = False

try:    
    purchase_total = float(purchase_total)
    if not(is_student_text == "" and purchase_total >= 0.0 and is_senior == ""):
        is_student_text = is_student_text.upper()
        is_senior = is_senior.upper()

        if (is_student_text == "YES" or is_student_text == "NO") and (is_senior == "YES" or is_senior == "NO"):

            discount_elegible = ( is_student_text== "YES" 
                                 and is_senior == "YES" 
                                 and purchase_total >= 1000 )
            
            if discount_elegible == True:
                final_total = purchase_total - (purchase_total*.10)
                print(f"final total: {final_total}")
            else:
                final_total = purchase_total
                print(f"final total: {final_total}")
        else:
            print("Error. Invalid input")
    else:
        print("Error.Verify you fill in all the information")
except:
    print("Eror: the purchase total only allow numbers")
print("---------------------------------------------------------------------")
print("-----------(Problem 4: Basic statistics of three integers)-----------")
#Problem 4: Basic statistics of three integers
"""
Descripción:
El programa solicita tres números enteros y calcula estadísticas básicas:
suma, promedio, valor máximo, valor mínimo y una bandera que indica si los
tres números son pares.

Entradas:
- n1, n2, n3 (int): números enteros proporcionados por el usuario.

Salidas:
- sum: suma de los tres números.
- average: promedio.
- max: número mayor.
- min: número menor.
- all_even: True si todos los números son pares.

Validaciones:
- Solo se aceptan números enteros.
- No se permiten valores vacíos.

Casos de prueba:
1) Normal:
   Input: 2, 4, 6
   Output: sum=12 | average=4.0 | max=6 | min=2 | all_even=True

2) Borde:
   Input: 2, 3, 4
   Output: sum=9 | average=3.0 | max=4 | min= 2 | all_even=False

3) Error:
   Input: "a", 2, 3
   Output: "Error, only integers are allowed"
--------------------------------------------------------------
"""


n1 = input("Enter the first number:").strip()
n2 = input("Enter the second number:").strip()
n3 = input("Enter the third number:").strip()

try:
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)

    sum_value =  n1 + n2 + n3
    average_value = sum_value / 3
    max_value = max(n1,n2,n3)
    min_value = min(n1, n2, n3)
    all_even = (n1 % 2 == 0) and (n2 % 2 == 0) and (n3 % 2 == 0)

    print(f"sum: {sum_value}")
    print(f"average: {average_value}")
    print(f"Max {max_value}")
    print(f"Min: {min_value}")
    print(f"all even: {all_even}")
except: 
    print("Error, only integers are allowed")


print("---------------------------------------------------------------------")
print("-------------------(Problema 5 : Loan elegibility)-------------------")
#Problem 5: Loan eligibility (income and debt ratio)
"""
Descripción:
El programa determina si un usuario califica para un préstamo usando tres
criterios:
- ingreso mensual mínimo de $8000,
- relación deuda/ingreso menor o igual a 0.40,
- puntaje crediticio igual o mayor a 650.

Entradas:
- monthly_income (float)
- monthly_debt (float)
- credit_score (int)

Salidas:
- debt_ratio: razón deuda/ingreso.
- eligible: bandera booleana que indica si califica.

Validaciones:
- Ingreso mensual debe ser > 0.
- Deuda mensual debe ser >= 0.
- Puntaje crediticio debe ser entero >= 0.
- Solo se aceptan valores numéricos.

Casos de prueba:
1) Normal:
   Input: income=9000, debt=2000, score=700
   Output: eligible=True

2) Borde:
   Input: income=8000, debt=3200, score=650
   Output: eligible=True

3) Error:
   Input: income="abc"
   Output: "Error. Invalid input, try again"
--------------------------------------------------------------
"""
monthly_income = input(" Enter the monthly income:").strip()
monthly_debt= input(" Enter the monthly debt: ").strip()
credit_score = input("Enter your credit score: ").strip()

try:
    monthly_debt = float(monthly_debt)
    monthly_income = float(monthly_income)
    credit_score = int(credit_score)

    eligible= False

    if monthly_income > 0.0 and monthly_debt>= 0.0 and credit_score >= 0:
        debt_ratio = monthly_debt / monthly_income
        eligible = (monthly_income >= 8000.0 and debt_ratio <= 0.4 and credit_score >= 650)
        print(f"debt_ratio: {debt_ratio}")
        print(f"Elegible: {eligible}")
    else:
        print("Error. Invalid input")
    

except:
    print("Error. Invalid input, try again")

print("---------------------------------------------------------------------")
print("---------(Problem 6: Body Mass Index (BMI) and category flag)--------")
#Problem 6: Body Mass Index (BMI) and category flag
"""
Descripción:
El programa calcula el índice de masa corporal (BMI) usando la fórmula:
BMI = peso_kg / (altura_m ** 2)
También genera tres banderas booleanas:
- is_underweight: BMI < 18.5
- is_normal: 18.5 <= BMI < 25
- is_overweight: BMI >= 25

Entradas:
- weight_kg (float)
- height_m (float)

Salidas:
- BMI redondeado a 2 decimales.
- Estado de las tres categorías en forma booleana.

Validaciones:
- Altura y peso deben ser mayores que 0.
- Solo se aceptan números reales.

Casos de prueba:
1) Normal:
   Input: weight=70, height=1.75
   Output: BMI=22.86, normal=True

2) Borde:
   Input: weight=50, height=1.80
   Output: underweight=True

3) Error:
   Input: weight="abc"
   Output: "Error only numbers are allowed"
--------------------------------------------------------------
"""

weight_kg= input("Enter your weight in kg: ").strip()
height_m= input("Enter your height in meters: ").strip()

try:
    weight_kg = float(weight_kg)
    height_m = float(height_m)

    if weight_kg > 0.0 and height_m > 0.0:
        bmi = weight_kg / (height_m * height_m)
        is_underweight = (bmi < 18.5)
        is_normal=  (18.5 <= bmi < 25.0)
        is_overweight = (bmi >= 25.0)

        print(f"BMI: {round(bmi,2)}")
        print(f"underweight: {is_underweight}")
        print(F"normal: {is_normal}")
        print(f"overweight: {is_overweight}")

    else:
        print("Error. Invalid input")
except:
    print("Error only numbers are allowed, try again")

#Reflexion
"""
En estos ejercicios se observa cómo los enteros y flotantes trabajan juntos para resolver
problemas del mundo real, como pagos, promedios o conversiones. Las comparaciones generan
valores booleanos que permiten decidir distintos caminos mediante estructuras if. Validar
rangos es esencial para evitar errores lógicos y matemáticos, como divisiones entre cero
o valores físicamente imposibles. También aprendí a combinar condiciones con and, or y not
para crear reglas más completas y precisas. Estos patrones se repiten constantemente en
aplicaciones como nómina, descuentos, préstamos o evaluaciones de salud, donde las decisiones
dependen del análisis correcto de números y condiciones lógicas.
"""
#Referencias
"""
1) Python Documentation – Built-in Types (int, float, bool)
2) W3Schools – Python Numbers & Operators
3) Real Python – Python Conditional Statements: if, elif, else
4) Programiz – Python User Input and Type 
5) Automate the Boring Stuff with Python – Numerical and Boolean Operations
"""

##Repositorio de github
"""
https://github.com/dNavarro-07/homework_projects.git
"""

