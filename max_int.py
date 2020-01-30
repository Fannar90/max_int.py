north_int = int(input("Number of cars travelling north: "))
south_int = int(input("Number of cars travelling south: "))
east_int = int(input("Number of cars travelling east: "))
west_int = int(input("Number of cars travelling west: "))

max_batch = 5

cars_north = north_int
print("Number of cars travelling north:",cars_north)
cars_south = south_int
print("Number of cars travelling south:",cars_south)
cars_east = east_int
print("NUmber of cars travelling east:",cars_east)
cars_west = west_int
print("Number of cars travelling west:",cars_west)

n_s = cars_north + cars_south
print("Cars travelling north and south",n_s)
e_w = cars_east + cars_west
print("Cars travelling east and west",e_w)

while n_s > max_batch:
    pass



