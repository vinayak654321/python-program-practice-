# -------------------------------
# 1. Simple Function
# -------------------------------

def greet():
    print("Hello, welcome to Python functions!")

greet()


# -------------------------------
# 2. Function with Arguments
# -------------------------------

def add(a, b):
    return a + b

result = add(10, 5)
print("Addition result:", result)


# -------------------------------
# 3. Function with *args
# -------------------------------

def sum_all(*args):
    total = 0
    for num in args:
        total += num
    return total

print("Sum using *args:", sum_all(1, 2, 3, 4, 5))


# -------------------------------
# 4. Function with **kwargs
# -------------------------------

def student_info(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)

student_info(name="Vinayak", age=21, course="Python")


# -------------------------------
# 5. Local vs Global Scope
# -------------------------------

x = 10  # Global variable

def scope_example():
    x = 5  # Local variable
    print("Inside function (local x):", x)

scope_example()
print("Outside function (global x):", x)
