
   
AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan', 'Rivian R1T', 'Ram 1500' ]

def WriteArraytoFile(array, filename="authorized_vehicles.txt"):
    with open(filename,"w" ) as file:
            for item in array:
                file.write(item + "\n")
    print(f"Written to file: {filename}")
WriteArraytoFile(AllowedVehiclesList)

def ReadArrayFromFile(filename="authorized_vehicles.txt"):
    with open(filename, "r") as file:
        return [line.strip() for line in file.readlines()]

def printV():
    print ("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
    VehiclesFromFile = ReadArrayFromFile()
    for i in VehiclesFromFile:
        print (i, end=" \n")
    menu()

def search():
    print ("Please Enter the full Vehicle name:")
    VehiclesFromFile = ReadArrayFromFile()
    z = str(input())
    if z in VehiclesFromFile:
        print(z + " is an authorized vehicle")
        menu()
    else:
        print(z + " is not an authorized vehicle, if you received this in error please check the spelling and try again")
        menu()
def add():
    print("Please Enter the full Vehicle name you would like to add:")
    VehiclesFromFile = ReadArrayFromFile()
    newVehicle = input()
    VehiclesFromFile.append(newVehicle)
    WriteArraytoFile(VehiclesFromFile)
    print(f'''you have added "{newVehicle}" as an authorized vehicle''')
    menu()

def delete():
    print("Please Enter the full Vehicle name you would like to REMOVE")
    removeVehicle = input()
    print(f'''Are you sure you want to remove "{removeVehicle}" from the Authorized Vehicles List?''')
    confirmInput = input()
    VehiclesFromFile = ReadArrayFromFile()
    if confirmInput == "yes":
        VehiclesFromFile.remove(removeVehicle)
        WriteArraytoFile(VehiclesFromFile)
        print(f'''You have REMOVED "{removeVehicle}" as an authorized vehicle''')
    else: 
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
        menu()

def menu():
    x = ("********************************\nAutoCountry Vehicle Finder v0.6\n********************************\nPlease Enter the following number below from the following menu:\n \n1. PRINT all Authorized Vehicles\n2. SEARCH for Authorized Vehicle\n3. ADD Authorized Vehicle\n4. DELETE Authorized Vehicle\n5. Exit")
    print (x)
    y = int(input())
    if y == 1:
        printV()
    if y == 2:
        search()
    if y == 3: 
        add()
    if y == 4: 
         delete()
    if y == 5:
        print ("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
menu()

