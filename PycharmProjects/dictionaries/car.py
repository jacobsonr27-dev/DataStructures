
cars = {}
while True:
    print("1: Register a car")
    print("2: Search a car")
    print("3: Exit")
    option = input("select and option: ")
    if option == '1':
        car_plate = input("Enter Licence Plate: ")
        car_make = input("Enter Make of Car: ")
        car_color = input("Enter Color of Car: ")
        car_year = input("Enter the year of the car(YYYY): ")
        cars[car_plate] = [car_make, car_color, car_year]
    elif option == '2':
        search = input("Enter the license plate number to search: ")
        if search in cars:
            print("Car Make: " + str(cars[search][0]))
            print("Car Color: " + str(cars[search][1]))
            print("Car Year: " + str(cars[search][2]))
        else:
            print("not a valid search")
    else:
        break
