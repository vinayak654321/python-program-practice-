name = input("Enter your name: ")
age = int(input("Enter your age: "))
marks = int(input("Enter your marks: "))

print("\n--- Student Report ---")

# Age condition
if age < 18:
    print("Status: Minor (Under 18)")
else:
    print("Status: Adult (18 or above)")

# Marks condition
if marks >= 75:
    print("Grade: Distinction")
elif marks >= 60:
    print("Grade: First Class")
elif marks >= 40:
    print("Grade: Pass")
else:
    print("Grade: Fail")
