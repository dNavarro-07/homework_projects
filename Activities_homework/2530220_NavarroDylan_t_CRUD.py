# ------------------------------------------------------------
# Manejo de bucles en Python
# Nombre: Navarro Hernández Dylan Alexander
# Matrícula: 2530220
# Grupo: IM-1:1
# ------------------------------------------------------------
#RESUMEN EJECUTIVO
"""
Un CRUD es un programa que permite gestionar datos mediante cuatro operaciones básicas: Create (crear), Read (leer),
Update (actualizar) y Delete (eliminar). Para este proyecto elegí usar un diccionario o una lista de diccionarios
porque permiten almacenar múltiples ítems de forma estructurada y acceder rápidamente por claves o índices.
El uso de funciones ayuda a separar cada operación del CRUD, haciendo el código más claro, modular y fácil de mantener.
El programa incluye un menú principal que permite al usuario seleccionar entre crear ítems nuevos, leer o buscar datos,
actualizarlos, eliminarlos y mostrar la lista completa de elementos almacenados.
"""

#DESCRIPCION DEL PROBLEMA
"""
Problem: In-memory CRUD manager with functions

Descripción:
Este programa implementa un gestor CRUD (Create, Read, Update, Delete) almacenando
los ítems en un diccionario en memoria. Cada ítem contiene los campos:
- name (string)
- price (float)
- quantity (int)

Se utilizan funciones separadas para cada operación (create_item, read_item,
update_item, delete_item, list_items) y un menú interactivo que permite al
usuario ejecutar cada acción mediante opciones numéricas.

Entradas:
- option (string): opción seleccionada del menú (0–5).
- Para CREATE:
    - item_id (string, no vacío)
    - name (string, no vacío)
    - price (float >= 0)
    - quantity (int >= 0)
- Para READ/UPDATE/DELETE:
    - item_id (string)
- Para UPDATE:
    - new_name (string)
    - new_price (float >= 0)
    - new_quantity (int >= 0)

Salidas:
- Mensajes según la operación:
    - "Item created"
    - "Item updated"
    - "Item deleted"
    - "Item found: {...}"
    - "Item not found"
    - "Items list:" (con impresión de todos los ítems)
    - O bien mensajes de error:
        - "Error: invalid input"
        - "Error: id already exists"

Validaciones:
- La opción del menú debe ser una cadena válida dentro de {"0","1","2","3","4","5"}.
- item_id y name no pueden estar vacíos en CREATE o UPDATE.
- price debe convertirse a float y ser >= 0.
- quantity debe convertirse a int y ser >= 0.
- No se permite crear un ítem cuyo id ya exista.
- READ, UPDATE y DELETE verifican si el id existe; si no, muestran "Item not found".
- LIST imprime "No items found." si el diccionario está vacío.

Casos de prueba:
1) Normal:
   - Crear un ítem, leerlo, actualizarlo y eliminarlo.
   - Resultado esperado: mensajes correctos y base de datos vacía al final.

2) Borde:
   - Crear un ítem con quantity = 0 o price = 0.
   - Leer ítem usando un id largo o con espacios (tras strip()).

3) Error:
   - Ingresar una opción fuera del menú → "Error: invalid input".
   - Intentar crear con price no numérico o negativo → "Error: invalid input".
   - Leer/actualizar/eliminar un id inexistente → "Item not found".
"""

"""
Implementación CRUD usando:
Estructura principal = diccionario: item_id -> datos del ítem.

Motivo:
Usar un dict permite búsquedas, actualizaciones y eliminaciones por id
de forma muy eficiente (O(1)). Además, garantiza unicidad natural de los IDs.
La alternativa con lista funciona pero requiere búsquedas lineales.
"""
def create_item(db, item_id, name, price, quantity):
    """Crea un ítem si el id NO existe. Regresa True si se creó."""
    if item_id in db:
        return False  # No permitir duplicados
    db[item_id] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }
    return True

 #Regresa el dict del ítem o None si no existe.
def read_item(db, item_id):
    return db.get(item_id)

#Actualiza un ítem existente. Regresa True si se actualizó.
def update_item(db, item_id, new_name, new_price, new_quantity):
  
    if item_id not in db:
        return False
    db[item_id]["name"] = new_name
    db[item_id]["price"] = new_price
    db[item_id]["quantity"] = new_quantity
    return True

# Elimina un ítem existente. Regresa True si se borró.
def delete_item(db, item_id):
    if item_id not in db:
        return False
    del db[item_id]
    return True

#Imprime todos los ítems. Regresa la lista de objetos.
def list_items(db):
    
    if not db:
        print("No items found.")
        return []

    print("Items list:")
    for item_id, info in db.items():
        print(f"- ID: {item_id}, Name: {info['name']}, Price: {info['price']}, Quantity: {info['quantity']}")
    return list(db.values())

def main():
    database = {}  # dict principal

    while True:
        print("\n----- CRUD Menu -----")
        print("1) Create item")
        print("2) Read item by id")
        print("3) Update item by id")
        print("4) Delete item by id")
        print("5) List all items")
        print("0) Exit")
        option = input("Choose option: ").strip()

        # --- Validar opción ---
        if option not in {"0", "1", "2", "3", "4", "5"}:
            print("Error: invalid input")
            continue

        if option == "0":
            print("Exiting program...")
            break

        # =====================================================
        # CREATE
        # =====================================================
        if option == "1":
            item_id = input("Enter item id: ").strip()
            name = input("Enter name: ").strip()
            price_text = input("Enter price: ").strip()
            quantity_text = input("Enter quantity: ").strip()

            if not item_id or not name:
                print("Error: invalid input")
                continue

            # Validar price y quantity
            try:
                price = float(price_text)
                quantity = int(quantity_text)
                if price < 0 or quantity < 0:
                    raise ValueError
            except:
                print("Error: invalid input")
                continue

            created = create_item(database, item_id, name, price, quantity)
            if created:
                print("Item created")
            else:
                print("Error: id already exists")

        # =====================================================
        # READ
        # =====================================================
        elif option == "2":
            item_id = input("Enter item id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            item = read_item(database, item_id)
            if item is None:
                print("Item not found")
            else:
                print("Item found:", item)

        # =====================================================
        # UPDATE
        # =====================================================
        elif option == "3":
            item_id = input("Enter item id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            name = input("Enter new name: ").strip()
            price_text = input("Enter new price: ").strip()
            quantity_text = input("Enter new quantity: ").strip()

            if not name:
                print("Error: invalid input")
                continue

            try:
                price = float(price_text)
                quantity = int(quantity_text)
                if price < 0 or quantity < 0:
                    raise ValueError
            except:
                print("Error: invalid input")
                continue

            updated = update_item(database, item_id, name, price, quantity)
            if updated:
                print("Item updated")
            else:
                print("Item not found")

        # =====================================================
        # DELETE
        # =====================================================
        elif option == "4":
            item_id = input("Enter item id: ").strip()
            if not item_id:
                print("Error: invalid input")
                continue

            deleted = delete_item(database, item_id)
            if deleted:
                print("Item deleted")
            else:
                print("Item not found")

        # =====================================================
        # LIST
        # =====================================================
        elif option == "5":
            list_items(database)


# Ejecutar si es el programa principal
if __name__ == "__main__":
    main()

#Conclusiones
"""
El uso de funciones simplificó mucho la implementación del CRUD porque permitió
dividir el programa en partes pequeñas, claras y reutilizables. Usar un diccionario
(or list of dicts) facilitó almacenar y acceder a los datos de cada ítem sin
complicaciones, especialmente al buscar por id. Durante el desarrollo, uno de los
problemas principales fue validar correctamente las entradas del usuario, ya que
cualquier dato vacío o no numérico podía romper el programa; esto se resolvió con
condiciones y manejo de excepciones. Este CRUD podría ampliarse guardando la
información en archivos JSON, CSV o en una base de datos real para hacerlo persistente
y apto para sistemas más grandes.
"""
#REFERENCIAS
"""
- Python documentation – Data structures (list, dict).
- Python documentation – Defining functions.
- Tutoriales básicos sobre CRUD en memoria con Python (Real Python, W3Schools).
"""

#REPOSITORIO DE GITHUB
"""
https://github.com/dNavarro-07/homework_projects
"""