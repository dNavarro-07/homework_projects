# ------------------------------------------------------------
# Manejo de strings en Python
# Nombre: Navarro Hernández Dylan Alexander
# Matrícula: 2530220
# Grupo: IM-1:1
# ------------------------------------------------------------


"""
RESUMEN EJECUTIVO:
Este documento cubre el uso de cadenas (strings) en Python, un tipo de dato inmutable
que permite realizar operaciones como concatenación, longitud, slicing, búsqueda y
reemplazo. A lo largo de seis problemas se aplican técnicas de normalización,
validación de entradas y manipulación de texto. Se incluyen descripciones,
validaciones y casos de prueba para cada ejercicio.


BUENAS PRÁCTICAS:
- Los strings son inmutables; cada cambio crea una nueva cadena.
- Usar strip() y lower() para normalizar antes de comparar.
- Evitar números mágicos; documentar los slices.
- Utilizar métodos de string en lugar de reprogramar funciones básicas.
- Validar entradas: primero que no estén vacías, después el formato.
- Mantener nombres claros y mensajes comprensibles.
"""

#PROBLEMAS
print("---------------------------------------------------------------------------------------")
print("--------------[Problema 1: full name formatter(name + initials)]-----------------------")

#Problem 1: Full name formatter (name + initials)
"""
Descripción:
El programa recibe un nombre completo, elimina espacios extra,
normaliza la capitalización usando Title Case y genera las
iniciales de cada palabra del nombre.

Entradas:
- full_name (string): nombre completo del usuario, puede contener
  espacios extra o letras en mayúsculas/minúsculas mezcladas.

Salidas:
- "initials: X.X.X."
- "Formatted name: Nombre En Title Case"

Validaciones:
- La entrada no puede quedar vacía después de strip().
- Debe contener al menos dos palabras.
- No se permiten cadenas formadas solo por espacios.

Casos de prueba:
1) Normal:
   Input: "dylan navarro hernandez"
   Output: Initials: D.N.H. | Formatted name: Dylan Navarro Hernandez

2) Borde:
   Input: "   MARIA   LOPEZ "
   Output: Initials: M.L. | Formatted name: Maria Lopez

3) Error:
   Input: " "
   Output: "enter a valid name"
--------------------------------------------------------------
"""


full_name = str(input("Enter your full name:").strip())
full_name = full_name.lower()
name_parts = full_name.split()

if full_name == "" or len(name_parts) < 2:
    print("enter a valid name")

else:
    formatted_name = " ".join(name_parts).title()

    initials = " "
    for parts in name_parts:
        initials += parts[0].upper() + "."
    
    print(f"initials: {initials}")
    print(f"Formatted name: {formatted_name}")


print("---------------------------------------------------------------------------------------")
print("--------------[Problema 2: Simple email validator (structure + domain)]----------------")
#Problem 2: Simple email validator (structure + domain)
"""
Descripción:
El programa valida si un correo electrónico tiene una estructura
correcta. Verifica que contenga exactamente un '@', que no tenga
espacios y que el dominio incluya almenos un punto.

Entradas:
- email_text (string): correo electrónico ingresado por el usuario.

Salidas:
- "Valid email: True" y "Domain: ejemplo.com"
- O un mensaje indicando que la estructura es incorrecta.

Validaciones:
- Debe existir exactamente un '@'.
- No debe contener espacios.
- Después del '@', el dominio debe contener al menos un punto.
- Maneja errores cuando el usuario no escribe un texto válido.

Casos de prueba:
1) Normal:
   Input: "pepepecas69@gmail.com"
   Output: Valid email: True | Domain: gmail.com

2) Borde:
   Input: "juan.76@upv.edu.mx"
   Output: "Valid email: True | Domain: upv.edu.mx"

3) Error:
   Input: "lola67@@gmail.com"
   Output: "-The email structure is wrong, try again."
--------------------------------------------------------------
"""

email_text= str(input("Enter your email: ").strip())
try:
    domain= email_text.split("@")[1]
except:
    print("-The email must have at least a '@'")

if email_text.count("@") == 1 and email_text.count(" ") == 0 and domain.count(".") >= 1:
    valid_email= True
else:
    valid_email = False

if valid_email == True:
    print(f"Valid email:{valid_email}")
    print(f"Domain:{domain}")
else:
    print("-The email structure is wrong, try  again.")


print("---------------------------------------------------------------------------------------")
print("----------------------------[Problema 3: Palindrome checker]---------------------------")
#Problem 3: Palindrome checker (ignoring spaces and case)
"""
Descripción:
El programa verifica si una frase es un palíndromo, ignorando
espacios. Solo considera válidos textos que contengan al menos
3 caracteres sin contar espacios.

Entradas:
- phrase (string): texto ingresado por el usuario.

Salidas:
- "Is palindrome: True" o "False"
- Mensajes de error si la cadena está vacía o es demasiado corta.

Validaciones:
- No puede ser una cadena vacía.
- Debe contener al menos 3 letras sin contar espacios.
- No se permiten entradas hechas solo de espacios.

Casos de prueba:
1) Normal:
   Input: "anita lava la tina"
   Output: Is palindrome: True

2) Borde:
   Input: "oso"
   Output: Is palindrome: True

3) Error:
   Input: " a "
   Output: "At least 3 characters without white spaces"
--------------------------------------------------------------
"""
phrase  = str(input("Palindrome checker. Enter your text: ").strip())
phrase_replace = phrase.replace(" ","").lower()


if not (phrase== "" or phrase_replace == "") :
    reverse_phrase = phrase_replace[::-1]

    if len(phrase_replace) >= 3:

        if phrase.replace(" ","").lower() == reverse_phrase  :
            Is_palindrome = True
        else:
            Is_palindrome = False

        print(f"Is palindrome: {Is_palindrome}")
    else:
        print("At least 3 characters without white spaces")
else:
    print("empty spaces are not allowed. Try again")

print("---------------------------------------------------------------------------------------")
print("---------------------------[Problema 4: Sentence word stats]---------------------------")
#Problem 4: Sentence word stats (lengths and first/last word)
"""
Descripción:
El programa analiza una oración y cuenta sus palabras. También
extrae la primera, la última, la palabra más corta y la más larga.

Entradas:
- sentence (string): oración escrita por el usuario.

Salidas:
- Cantidad de palabras
- Primera y última palabra
- Palabra más corta y más larga

Validaciones:
- La oración no puede estar vacía.
- Debe contener al menos 2 palabras.

Casos de prueba:
1) Normal:
   Input: "The Upv is poor"
   Output: 
        word count: 4
        First word: The
        last word: poor
        shortest word: is
        longest word: poor
2) Borde:
   Input: "teacher charly"
   Output: 
        word count: 2
        First word: teacher
        last word: charly
        shortest word: charly
        longest word: teacher

3) Error:
   Input: "   hello   "
   Output: "The sentence cannot be empty or shorter than 2 words"
--------------------------------------------------------------
"""
sentence = str(input("Write a sentence:")).strip()
sentence_words = sentence.split()
word_count = len(sentence_words)

if not sentence == "" and word_count > 1:

    first_word = sentence_words[0]
    last_word = sentence_words[-1]
    
    print(f"word count: {word_count}")
    print(f"First word: {first_word}")
    print(f"last word: {last_word}")

    shortest_word = sentence_words[0]
    longest_word = sentence_words[0]
    
    for word in sentence_words:
        if len(word) > len(longest_word):
            longest_word = word
        if len(word) < len (shortest_word):
            shortest_word = word
    

    print(f"shortest word: {shortest_word}")
    print(f"longest word: {longest_word}")
else:
    print("The sentence cannot be empty or shorter than 2 words")

print("---------------------------------------------------------------------------------------")
print("--------------------[Problema 5: password strength classifier]-------------------------")
#Problem 5: Password strength classifier
"""
Descripción:
El programa clasifica la fortaleza de una contraseña según:
longitud, mayúsculas, minúsculas, números y símbolos.

Entradas:
- password_input (string): contraseña escrita por el usuario.

Salidas:
- "Password_strength: strong/medium/weak"

Validaciones:
- Debe tener mínimo 4 caracteres.
- La clasificación depende de las combinaciones encontradas.

Criterios:
- Strong: >= 8 caracteres, minúsculas, mayúsculas, números y símbolos.
- Medium: >= 8 caracteres y mezcla básica (mayús/minús o dígitos).
- Weak: todo lo demás (< 8).

Casos de prueba:
1) Fuerte:
   Input: "Abc123$%"
   Output: "password strength: strong"

2) Media:
   Input: "Password1"
   Output: "password strength: medium"

3) Débil:
   Input: "abcd3"
   Output: "password strength: weak"
4) Error:
    input: "a23"
    Output: "The password must have at least 4 characters. Try again"
--------------------------------------------------------------
"""
password_input = str(input("Password classifier. Enter a password:"))

has_upper = False
has_lower = False
has_digit = False
has_symbol = False
password_strength = ""
if not password_input == "" and len(password_input) >= 4:
    for character in password_input:
        if character.islower():
            has_lower = True
        if character.isupper():
            has_upper = True
        if character.isdigit():
            has_digit = True
        if not character.isalnum():
            has_symbol = True

    if len(password_input) >= 8 and has_digit and has_lower and has_symbol and has_upper : 
     password_strength = "strong"
    elif len(password_input) >= 8 and ((has_upper and has_lower) or has_digit):
       password_strength = "medium"
    else:
        password_strength = "weak"
    
    print(f"Password strength: {password_strength}")
else:
    print("The password must have at least 4 characters. Try again")

print("---------------------------------------------------------------------------------------")
print("---------------------[Problema 6: product label formatter]-----------------------------")
#Problem 6: Product label formatter (fixed-width text)
"""
Descripción:
El programa genera una etiqueta de producto en formato fijo.  
La etiqueta contiene el nombre del producto y su precio, con este formato:

    Product: <nombre> | Price: $<precio>

Luego la etiqueta se ajusta para que tenga exactamente **30 caracteres**:
- Si es más corta, se rellenan espacios al final.
- Si es más larga, se recorta a los primeros 30 caracteres.

Entradas:
- Product_name (string): nombre del producto ingresado por el usuario.
- price_value (string): texto que debe convertirse a número (float).

Salidas (dependiendo del caso):
- Si todo es válido:
      label: Product: <Product_name> | Price: $<price_formateado>
  (La etiqueta siempre mide 30 caracteres exactos)

- Si el nombre está vacío:
      "The product name is empty"

- Si el precio no es numérico:
      "The price must be numbers"

- Si el precio es numérico pero negativo:
      "The price was entered wrong"

Validaciones:
- El nombre no puede quedar vacío después de strip().
- El precio debe poder convertirse a float.
- El precio debe ser mayor o igual a 0.

Casos de prueba:
1) Normal:
   Input:
        Product_name = "Manzana"
        price_value = "12.5"
   Output:
        label: Product: Manzana | Price: $12.5  

   (Si mide menos de 30 caracteres, el programa agrega espacios hasta llegar a 30)

2) Borde — nombre muy largo:
   Input:
        Product_name = "ChocolateAmargoPremiumDeluxe"
        price_value = "50"
   Output:
        label: Product: ChocolateAmargoPremium
   (Se recortan los caracteres extra para dejar la etiqueta en 30)

3) Error — precio negativo:
   Input:
        Product_name = "Refresco"
        price_value = "-5"
   Output:
        "The price was entered wrong"

4) Error — precio no numérico:
   Input:
        Product_name = "Goma"
        price_value = "abc"
   Output:
        "The price must be numbers"

--------------------------------------------------------------
"""
Product_name = str(input("Eenter the product name:").strip())
price_value = (input("Enter its price: ").strip())

if Product_name == "":
    print("The product name is empty")
else:
    try:
        price= float(price_value)
        if price >= 0:
            price_str= str(price)
            label = (f"Product: {Product_name} | Price: ${price_str} ")

            letter_counter = len(label)

            if letter_counter <= 30:
                label = label + " "*(30-letter_counter) + "'"
            else:
                  label= label[:30]

            print(f"label:{label}")
        else: 
            print("The price was entered wrong")
    except:
        print("The price must be numbers")

print("--------------------------------------------------------------------------------")

# ConclusioneS
"""
El manejo de strings es fundamental para procesar entradas y generar salidas claras y útiles. Funciones como lower(), strip(), 
split() y join() permiten limpiar, transformar y estructurar texto de manera eficiente, lo cual es clave en cualquier programa 
que interactúe con el usuario. Normalizar texto antes de compararlo evita errores por mayúsculas, espacios o formatos 
inconsistentes. Además, las validaciones bien diseñadas ayudan a prevenir datos basura y aseguran que el programa funcione 
correctamente. A lo largo de este trabajo también se refuerza la importancia de la inmutabilidad de los strings, que obliga a 
crear nuevas variables al modificarlos, y del uso de slices para invertir o seleccionar partes del texto, como en el verificador 
de palíndromos.
-------------------------------------------------------------------------------------------------------------
"""

#Referencias
"""
1) Python Documentation – Built-in Types: Text Sequence Type — str
2) W3Schools – Python Strings
3) Real Python – Working With Strings in Python
4) Automate the Boring Stuff with Python – Chapter on Strings
5) Programiz – Python String Methods
"""

#Repositorio de github
"""
https://github.com/dNavarro-07/homework_projects.git
"""






