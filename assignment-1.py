#section 1
name = "Sofia"
age = 20
height = 5.4
is_student = True

print(name, type(name))
print(age, type(age))
print(height, type(height))
print(is_student, type(is_student))

userName = input("Hello! What is your name?")
birthYear = input("Awesome! What year were you born in?")
birthYear = int(birthYear)
userAge = (2026 - birthYear)

#section 2
print("Hi,", userName, "! You are approximately", userAge, "years old")

#section 3
numOne = input("Input a number.")
numOne = (float(numOne))
numTwo = input("great! Input another number.")
numTwo = (float(numTwo))

answer = float(numOne * numTwo)
print(numOne, "x", numTwo, "=", answer)

#section 4
print("===========================")
print("        RECEIPT            ")
print("===========================")
print("Item:      PRIMA CD")
print("Price:     $11.99")
print("Quantity:  1")
print("---------------------------")
print("Total:     $11.99")
print("===========================")

#Section 5
homeTown = input("What is your hometown?")
hobby = input("What is one of your hobbies?")
funFact = input("What is one fun fact about you?")

print("╔══════════════════════════════╗")
print("        PROFILE:", name)
print("╚══════════════════════════════╝")
print("Hometown:", homeTown)
print("Hobby:", hobby)
print("Fun Fact:", funFact)
print("Age:", userAge)
