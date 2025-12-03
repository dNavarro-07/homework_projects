# ------------------------------------------------------------
# Manejo de Listas, Tuplas y Diccionarios en Python
# Nombre: Navarro Hernández Dylan Alexander
# Matrícula: 2530220
# Grupo: IM-1:1
# ------------------------------------------------------------

#RESUMEN EJECUTIVO
"""
En Python, una lista es una colección ordenada y mutable, lo que permite 
agregar, eliminar o modificar elementos. Una tupla es similar a una lista, 
pero es inmutable, por lo que sus valores no pueden cambiar después de ser 
creada. Los diccionarios almacenan pares clave–valor y permiten búsquedas 
rápidas mediante una clave en lugar de un índice.
Este documento describe cada problema, el diseño de entradas y salidas, las 
validaciones necesarias y el uso de listas, tuplas y diccionarios en contextos 
prácticos como catálogos, registros y estadísticas. También se explica por qué 
la mutabilidad o inmutabilidad influye en la elección de cada estructura.
"""
#PRINCIPIOS Y BUENAS PRÁCTICAS
"""
- Usar listas cuando se necesite agregar, eliminar o modificar elementos frecuentemente.
- Usar tuplas para datos que deben mantenerse fijos, como coordenadas o configuraciones.
- Usar diccionarios cuando se requiera buscar información por una clave (nombre, id, código).
- Evitar modificar listas mientras se recorren con un ciclo for, para evitar errores lógicos.
- Elegir claves descriptivas en los diccionarios como "name", "price" o "quantity".
- Escribir código legible con nombres de variables claros y mensajes comprensibles para el usuario.
"""

print("---------------------------------------------------------------------")
print("-----------------(Problema 1: Shopping lists basics )----------------")
#Problem 1: Shopping list basics (list operations)
"""
Descripción:
El programa gestiona una lista de compras. Toma una lista inicial de productos,
agrega un nuevo artículo y verifica si un artículo buscado se encuentra dentro de
la lista final. También muestra la cantidad total de elementos.

Entradas:
- initial_inputs (str): cadena con artículos separados por coma.
- new_item (str): artículo a agregar.
- search_item (str): artículo a buscar dentro de la lista.

Salidas:
- items_list (list): lista final de artículos.
- len_list (int): cantidad total de artículos.
- found_item (bool): True si el artículo buscado está en la lista.

Validaciones:
- Ninguna de las entradas debe estar vacía.
- Los artículos deben ser texto.
- La entrada inicial debe tener al menos un elemento.
- Todo el texto se normaliza a minúsculas.

Casos de prueba:
1) Normal:
   Input:
      initial_inputs="apple, banana, milk"
      new_item="grapes"
      search_item="banana"
   Output:
      Items list: ['apple','banana','milk','grapes']
      Total items: 4
      Found item: True

2) Borde:
   Input:
      initial_inputs="bread"
      new_item="eggs"
      search_item="ham"
   Output:
      Items list: ['bread','eggs']
      Total items: 2
      Found item: False

3) Error:
   Input:
      initial_inputs=""
   Output:
      "Empty entries are not allowed"
--------------------------------------------------------------
"""
initial_inputs = str(input("Enter your shopping( For example: apple , banana, watermelon ):")). strip().lower()
new_item = str(input("Enter the new item: ")).strip().lower()
search_item = str(input("Enter the item to search:")).strip().lower()

if not (initial_inputs == "" or new_item == "" or search_item == ""):
    initial_inputs = initial_inputs.split(",")
    initial_inputs.append(new_item)
    items_list = initial_inputs
    print(f"Items list: {items_list}")

    len_list = len(items_list)
    print(f"Total items: {len_list}")

    found_item = search_item in items_list
    print(f"Found item: {found_item}")
else:
    print("Empty entries are not allowed")

print("---------------------------------------------------------------------")
print("--------(Problema 2: Points and distances with tuples )--------------")

#Problem 2: Points and distances with tuples
"""
Descripción:
El programa calcula la distancia entre dos puntos en el plano y también obtiene
el punto medio entre ellos. Usa tuplas para representar las coordenadas.

Entradas:
- x1 (str → float): coordenada x del punto A.
- y1 (str → float): coordenada y del punto A.
- x2 (str → float): coordenada x del punto B.
- y2 (str → float): coordenada y del punto B.

Salidas:
- point_a (tuple): (x1, y1)
- point_b (tuple): (x2, y2)
- distance (float): distancia entre A y B redondeada a 3 decimales.
- Midpoint (tuple): punto medio entre A y B.

Validaciones:
- Todos los valores deben ser numéricos.
- Si alguno no es convertible a float, se muestra error.

Casos de prueba:
1) Normal:
   Input: x1=0, y1=0, x2=3, y2=4
   Output:
      Point A: (0,0)
      Point B: (3,4)
      Distance: 5.000
      Midpoint: (1.5,2.0)

2) Borde:
   Input: x1=2, y1=2, x2=2, y2=2
   Output:
      Distance: 0.000
      Midpoint: (2,2)

3) Error:
   Input: x1="abc"
   Output:
      "Only numbers are allowed"
--------------------------------------------------------------
"""
print("Enter the values of the coordinates : (x1, y1) and (x2, y2)")
x1 = input("x1:").strip()
y1 = input("y1:").strip()
x2 = input("x2:").strip()
y2 = input("y2:").strip()

try:
    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    point_a = (x1, y1)
    point_b = (x2, y2)
    distance = round(((x2 - x1)**2 + (y2 - y1)**2)**0.5,3)
    Midpoint = ((x1 + x2)/2, (y1 + y2)/2)

    print(f"Point A: {point_a}")
    print(f"point B: {point_b}")
    print(f"Distance: {distance}")
    print(f"Midpoint: {Midpoint}")
except:
    print("Only numbers are allowed")

print("---------------------------------------------------------------------")
print("----------(Problema 3: Product catalog with dictionary)--------------")
# Problem 3: Product catalog with dictionary
"""
Descripción:
El programa simula un catálogo de productos usando un diccionario. El usuario
ingresa el nombre de un producto y la cantidad deseada, y el programa calcula el
precio total si el producto existe.

Entradas:
- product_name (str): nombre del producto a comprar.
- quantity (str → float): cantidad solicitada.

Salidas:
- unit_price (float): precio unitario del producto.
- quantity (float): cantidad ingresada.
- total_price (float): costo total calculado.

Validaciones:
- quantity debe ser numérico y mayor que 0.
- product_name no debe estar vacío.
- El producto debe existir en PRODUCT_LIST.
- Cualquier conversión inválida produce un error.

Casos de prueba:
1) Normal:
   Input: product_name="camisa", quantity=2
   Output:
      Unit price: 300
      Total: 600

2) Borde:
   Input: product_name="zapatos", quantity=1
   Output:
      Total: 200

3) Error (producto no existe):
   Input: product_name="gorra", quantity=2
   Output:
      "Error. Product not found"

4) Error (cantidad inválida):
   Input: product_name="camisa", quantity="abc"
   Output:
      "Only integers are allowed"
--------------------------------------------------------------
"""

PRODUCT_LIST = {
    "camisa": 300,
    "pantalon": 400,
    "zapatos" : 200
}

print(f"catalog: {list(PRODUCT_LIST.keys())}")
product_name = input("What you want to buy: ").strip().lower()
quantity = input("quantity: ")

try:
    quantity = float(quantity)

    if quantity > 0 and not product_name == "":

        if product_name in PRODUCT_LIST:
            unit_price = PRODUCT_LIST[product_name]
            print(f"Unit price: {unit_price}")

            print(f"Quantity: {quantity}")

            total_price = unit_price * quantity
            print(f"Total: {total_price}")
        else: 
            print("Error. Product not found")
    else:
        print("Invalid inputs")
except:
    print("Only integers are allowed")

print("---------------------------------------------------------------------")
print("----------(Problema 4: Student grades with dict and list)------------")
#Problem 4: Student grades with dict and list
"""
Descripción:
El programa almacena calificaciones de estudiantes usando un diccionario. El
usuario ingresa el nombre del estudiante y el programa muestra sus calificaciones,
calcula el promedio y determina si aprobó.

Entradas:
- Search_student (str): nombre del estudiante a buscar.

Salidas:
- grades_list (list): calificaciones del estudiante.
- average (float): promedio redondeado a 2 decimales.
- passed (bool): True si el promedio es >= 70.

Validaciones:
- Search_student no debe estar vacío.
- El estudiante debe existir en el diccionario.

Casos de prueba:
1) Normal:
   Input: Search_student="Dylan"
   Output:
      Grades: [60,75,87]
      average: 74.00
      Passed: True

2) Borde:
   Input: Search_student="David"
   Output:
      average: ~65.3
      Passed: False

3) Error:
   Input: Search_student="Pedro"
   Output:
      "Error. Student not found"
--------------------------------------------------------------
"""

students_list = {
    "Dylan": [60, 75, 87],
    "Anuar": [100, 95, 89],
    "David": [64, 60, 72],
    "Angel": [65,85,60]
}
print(f"students:{list(students_list.keys())}")

Search_student= input("Student to search: ").strip().title()

if not Search_student == "":
    if Search_student in students_list:
        grades_list = students_list[Search_student]
        print(f"Grades: {grades_list}")

        average = round((sum(students_list[Search_student])  / len(students_list[Search_student])),2)
        print(f"average: {average}")

        passed = average >= 70
        print(f"Passed: {passed}")
    else:
        print("Error. Student not found")

else:
    print("Error. Invalid name")
print("---------------------------------------------------------------------")
print("---------(Problema 5: Word frequency counter (list + dict))----------")
sentence = input("Enter a sentence: ").strip().lower()
#Word frequency counter (list + dict)
"""
Descripción:
El programa cuenta la frecuencia de cada palabra en una oración. Limpia signos
de puntuación, separa las palabras y muestra la palabra con mayor frecuencia.

Entradas:
- sentence (str): oración ingresada por el usuario.

Salidas:
- word_list (list): lista de palabras procesadas.
- freq_dict (dict): diccionario con frecuencias.
- common_word (str): palabra más frecuente.

Validaciones:
- La oración no debe estar vacía.
- Se remueven "." y "," antes de procesar.

Casos de prueba:
1) Normal:
   Input: "hello world hello again"
   Output:
      word_list: ["hello","world","hello","again"]
      Frequencies: {"hello":2,"world":1,"again":1}
      Most common word: hello

2) Borde:
   Input: "one"
   Output:
      Most common word: one

3) Error:
   Input: ""
   Output:
      "Error. Empty input"
--------------------------------------------------------------
"""

if not sentence == "":
    sentence_replace = sentence.replace("."," ").replace(","," ")
    word_list = sentence_replace.split()

    print(f"word list: {word_list}")

    freq_dict= {}

    for word in word_list:
        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1 
    print(f"Frequencies: {freq_dict}")

    common_word = ""
    max_frequency = 0
    for word, frequency in freq_dict.items():
        if frequency > max_frequency:
            max_frequency = frequency
            common_word = word
    print(f"Most common word: {common_word}")
else:
    print("Error. Empty imput")


print("---------------------------------------------------------------------")
print("---------(Problema 6: Simple contact book (dictionary CRUD))---------")
#Problem 6: Simple contact book (dictionary CRUD)
"""
Descripción:
El programa maneja un libro de contactos básico usando un diccionario. Permite
agregar, buscar o eliminar contactos según la acción seleccionada.

Entradas:
- action_text (str): acción a realizar ("ADD", "SEARCH", "DELETE").
- contact (str): nombre del contacto.
- phone (str) (solo en ADD): número telefónico a guardar.

Salidas:
- Mensajes según acción:
  - Contact saved
  - Phone: <número>
  - Contact deleted
  - Error si el contacto no existe o si la acción es inválida.

Validaciones:
- action_text debe ser ADD, SEARCH o DELETE.
- contact no debe estar vacío.
- phone no debe estar vacío en ADD.
- Si SEARCH o DELETE se ejecutan con un contacto inexistente, se muestra error.

Casos de prueba:
1) Normal (ADD):
   Input: action_text="ADD", contact="Alice", phone="5559998888"
   Output: "Contact saved: Alice, 5559998888"

2) Normal (SEARCH):
   Input: action_text="SEARCH", contact="Bob"
   Output: "Phone: 5559876543"

3) Normal (DELETE):
   Input: action_text="DELETE", contact="Carlos"
   Output: "Contact deleted: Carlos"

4) Error (acción inválida):
   Input: action_text="EDIT"
   Output: "Error. Invalid input"

5) Error (contacto no existe):
   Input: action_text="SEARCH", contact="Pedro"
   Output: "Error: contact not found"
--------------------------------------------------------------
"""

initial_contacts = {
    "Alice": "5551234567",
    "Bob": "5559876543",
    "Carlos": "5552468100",
    "Dylan": "2345677698",
    "Josue": "6967435673"
}
print(f"Contacts: {list(initial_contacts.keys())}")
print(f"Options: ADD, SEARCH, DELETE")
action_text = input("your option: ").strip().upper()
contact= input("Contact name: ").strip().title()

if action_text == "ADD":
    phone = input("Enter Phone: ").strip()
    if not phone == "":
        print(f"Contact saved: {contact}, {phone}")

elif action_text == "SEARCH" or action_text == "DELETE":
    if contact in initial_contacts:
        if action_text == "SEARCH":
            phone = initial_contacts[contact]
            print(f"Phone: {phone}")
        else: 
            initial_contacts.pop(contact)
            print(f"Contact deleted: {contact}")
    else:
        print("Error: contact not found")
else:
    print("Error. Invalid input")


#Conclusiones
"""
Las listas demostraron ser útiles cuando se necesita agregar, eliminar o modificar elementos con libertad, como en 
las listas de compras o en el conteo de palabras. Las tuplas funcionaron bien para representar datos fijos como coordenadas,
ya que su inmutabilidad evita cambios accidentales. Los diccionarios facilitaron búsquedas rápidas por clave, lo que permitió 
crear catálogos, contactos y registros de estudiantes. Un patrón común fue el uso de diccionarios que almacenan listas, 
combinando flexibilidad con acceso rápido. Estas estructuras, usadas juntas, permiten resolver problemas reales de forma clara,
organizada y eficiente.
"""
#Referencias
"""
1) Python documentation – Built-in Types: list, tuple, dict.
2) Python documentation – String Methods.
3) W3Schools – Python Data Structures (lists, tuples, dictionaries).
4) Real Python – Working With Collections in Python.
5) Automate the Boring Stuff with Python – Capítulos de estructuras de datos.
"""
#Repositorio de github
"""
https://github.com/dNavarro-07/homework_projects
"""
