print("----- FOR LOOP EXAMPLES -----")

# for loop with range
for i in range(1, 6):
    print("Number:", i)

print("\n----- FOR LOOP WITH LIST -----")

fruits = ["apple", "banana", "mango"]
for fruit in fruits:
    print(fruit)

print("\n----- WHILE LOOP EXAMPLE -----")

count = 1
while count <= 5:
    print("Count:", count)
    count += 1

print("\n----- LOOP CONTROL: break -----")

for i in range(1, 10):
    if i == 5:
        break
    print(i)

print("\n----- LOOP CONTROL: continue -----")

for i in range(1, 6):
    if i == 3:
        continue
    print(i)

print("\n----- LOOP CONTROL: pass -----")

for i in range(1, 4):
    if i == 2:
        pass
    print(i)

print("\n----- LIST COMPREHENSION -----")

numbers = [1, 2, 3, 4, 5]

# normal loop
squares = []
for n in numbers:
    squares.append(n * n)

print("Squares using loop:", squares)

# list comprehension
squares_comp = [n * n for n in numbers]
print("Squares using list comprehension:", squares_comp)
