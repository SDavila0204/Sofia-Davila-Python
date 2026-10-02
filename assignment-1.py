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
print(f"{numOne} x {numTwo} = {answer}")

#section 4
item = "PRIMA CD"
price = 11.99
quantity = 1
total = price * quantity

print("===========================")
print("        RECEIPT            ")
print("===========================")
print(f"Item:               {item}")
print(f"Price:        ${price:.2f}")
print(f"Quantity:       {quantity}")
print("---------------------------")
print(f"Total:        ${total:.2f}")
print("===========================")


#Section 5
homeTown = input("What is your hometown?")
hobby = input("What is one of your hobbies?")
funFact = input("What is one fun fact about you?")

print("╔══════════════════════════════╗")
print(f"        PROFILE: {name}")
print("╚══════════════════════════════╝")
print(f"Hometown: {homeTown}")
print(f"Hobby: {hobby}")
print(f"Fun Fact: {funFact}")
print(f"Age: {userAge}")
