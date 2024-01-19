# FUNCTIONS
fam3 = [1.73, 1.68, 1.71, 1.89]
print(max(fam3)) # 1.89
tallest = max(fam3)
print(tallest) # 1.89

print(round(1.68, 1)) # 1.7
print(round(1.68)) # 2.0

print(len(fam3))

# sort
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

full = first + second

full_sorted1 = sorted(full)
full_sorted2 = sorted(full, reverse = True)
print(full.reverse())

print(full_sorted1) # [9.5, 10.75, 11.25, 18.0, 20.0]
print(full_sorted2) # [20.0, 18.0, 11.25, 10.75, 9.5]

# METHODS
arr = ["liz",1.73,"emma",1.68,"sue",1.84,1.68]
print(arr.index("liz")) # 0
print(arr.count(1.68)) # 2
print(arr.count(1.73)) # 1

sister = "liz"
print(sister.capitalize()) # Liz
print(sister.replace("z","sa")) # lisa
print(sister.replace("liz","sue")) # sue
print(sister.index("z")) # 2

# append and delete
new_item = ["me",1.68]
house.append(new_item) # [['hallway', 11.25], ['kitchen', 2], ['living room', 20.0], ['bedroom', 10.75], ['bathroom', 9.5], ['me', 1.68]]
print(house)
del(house[1])
print(house) # [['hallway', 11.25], ['living room', 20.0], ['bedroom', 10.75], ['bathroom', 9.5], ['me', 1.68]]

place = "poolhouse"
print(place.upper()) # POOLHOUSE
print(place.count("o")) # 3