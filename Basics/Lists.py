
# LISTS
fam = ["dad",1.73, 1.68, 1.84, 1.92]
fam2 = [["liz",1.73],
        ["emma",1.68],
        ["sue",1.84]]
print(fam2)

#
hall = 11.25
kit = 18.0
liv = 20.0
areas = [hall, kit, liv]
print(areas)

# Subsetting List
print(fam[0])
print(fam[1])
print(fam[2:5]) # [start : end]

# slice
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]
eat_sleep_area = areas[3] + areas[7]
print(eat_sleep_area)
downstairs = areas[:6]
upstairs = areas[6:]

#
house = [["hallway", 11.25],
         ["kitchen", 18.0],
         ["living room", 20.0],
         ["bedroom", 10.75],
         ["bathroom", 9.50]]
bathroom_area = house[-1][1] # 9.50
print(house[1][1])
house[1][1] = 2
print(house[1][1])

# add item
areas_1 = areas + ["poolhouse", 24.5]
areas_2 = areas_1 + ["garage", 15.45]
print("Original areas list:", areas)
print("Extended areas with poolhouse:", areas_1)
print("Further extended areas with garage:", areas_2)

areas = [11.25, 18.0, 20.0, 10.75, 9.50]
areas_copy = areas[:]
areas_copy[0] = 5.0
print(areas) # [11.25, 18.0, 20.0, 10.75, 9.5]
print(areas_copy) # [5.0, 18.0, 20.0, 10.75, 9.5]