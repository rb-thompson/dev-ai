# Outputting data
mydata = {
    "name": "Rama",
    "age": 30,
    "city": "New York"
}

print(mydata["name"])  # Output: Rama
print(mydata["age"])   # Output: 30
print(mydata["city"])  # Output: New York

print(mydata)  # Output: {'name': 'Rama', 'age': 30, 'city': 'New York'}



# Inputting data
user_data = input("Enter your name: ")
print("Hello, " + user_data + "!")  # Output: Hello, [user's name]!



# Variables
x = 5
y = 10
z = x + y
print(z)  # Output: 15

API_URL = "https://api.example.com/data"
print(API_URL)  # Output: https://api.example.com/data



# Reading integer type data
age = int(input("Enter your age: "))
print("Your age is " + str(age) + ".")  # Output: Your age is [user's age].



# Formatting Output (Part 1)
print("Hello, {}! You are {} years old.".format(user_data, age))  # Output: Hello, [user's name]! You are [user's age] years old.



# Simple Conditional Statement
skill_level = input("Enter your skill level (1-10): ")
skill = int(skill_level)

if skill >= 10:
    print("You are a master chef!")