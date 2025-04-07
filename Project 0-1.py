def x_function():
    AllowedVehiclesList = [ 'Ford F-150', 'Chevrolet Silverado', 'Tesla CyberTruck', 'Toyota Tundra', 'Nissan Titan' ]
    x = ("********************************\nAutoCountry Vehicle Finder v0.1\n********************************\nPlease Enter the following number below from the following menu:\n \n1. PRINT all Authorized Vehicles\n2. Exit")
    print (x)
    y = int(input())
    if y == 1:
        print ("The AutoCountry sales manager has authorized the purchase and selling of the following vehicles: ")
        for i in AllowedVehiclesList:
            print (i, end=" \n")
        x_function()
    if y == 2:
        print("Thank you for using the AutoCountry Vehicle Finder, good-bye!")
x_function()