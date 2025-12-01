print("---------------------------------------------------------------------")
print("-----------------(Problema 1: Shopping lists basics )----------------")
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
    print
except:
    print("Only numbers are allowed")

print("---------------------------------------------------------------------")
print("---------(Problema 3: Product catalog with dictionary)--------------")

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

