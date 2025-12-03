print("----------------------------------------------------------------------")
print("-----(Problem 1: Rectangle area and perimeter (basic functions))------")
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


