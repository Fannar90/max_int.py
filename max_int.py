north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))

max_batch = 5

while (north_int + south_int + east_int + west_int) >0:

    if (north_int + south_int) >= (east_int + west_int):
        print("Green light on N/S")

        if north_int <= max_batch:
            north_int = 0
        else:
            north_int = north_int - max_batch
    

        if south_int <= max_batch:
            south_int = 0
        else:
            south_int = south_int - max_batch

    else:
        print("Green light on E/W")

        if east_int <= max_batch:
            east_int = 0
        else:
            east_int = east_int - max_batch


        if west_int <= max_batch:
            west_int = 0
        else:
            west_int = west_int - max_batch

         
      
print("No cars waiting, the traffic jam has been solved!")
