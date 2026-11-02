 # How to print any line in python
print("Hello World")


# Variable and datatypes
# How to define any variable
a = 5           #here a is variable name and 5 is the value which is of integer datatype
b = "Wasif"     #here b is variable name and Wasif is the value which is written in "" thats why it is an string
c = 3.14        #here c is variable name and 3.14 is the value and because it is an decimal number that why it is Float datatype
d = "2.32"      #here d is variable name and "2.32" is the value but because it is written in "" it is an String Datatype
e = True        #here e is variable name and True is the value and it is called as Boolean datatype(Only has two values True or False)


#how to take input from the user
A = input("What is your Name :- ")  #here we are taking input from the user in the default datatype which is string and saving it in A variable
print("Hello" , A)                  #here we are printing the stored value of A

B = int(input("How old are you :- "))   #here we change the default datatype to integer by adding int()
print("you are",B ,"year old")

C = float(input("What is the value of pi :- "))
print("The value of pi is ", C)


#Type casting

#type() function :
print(type(A)) 
print(type(B))
#with the help of Type() function we can find out what datatype the variable is storing

#Type Conversion
print(float(B)) #by this conversion from int to float if i enter 25 in the B variable the output of this line will be 25.0
print(int(C))   #by this conversion from float to int if i enter 3.14 in the C variabel the output of this line will be 3 (Rounding off)


#Operators
#Arithmatic Operators

#Addition
Add = 5 + 5
print(Add)

#Substraction
Sub = 25 - 5
print(Sub)
#Same goes for multiplication

#Division
div1 = 5/2  #if we use single / then output will be in float
div2 = 5//2 #if we use // then output will be in int
#To find Remainder of the division
div3 = 5%2 #output will be 1

#for power
pow2 = 2**2 #output will be 4
pow3 = 2**3 #output will be 8
pow4 = 2**4 #output will be 16


#Comparision Operators

# Equal to ==
Eq = 2 == 2
Eq1 = 2 == 3
print(Eq) #output will be true(Boolean) because 2 = 2
print(Eq1) #output will be false(Boolean) because 2 is not equal to 3

# Not Equal to != 
#Same ad Equal To 2 conditions

#More are
'''
greater than(>)
less than(<)
greater than equal to(>=)
less than equal to(<=)
'''

#Logical operators

# And Operator                     
username = "Wasif"
password = "wasif.20079"

if username == "Wasif" and password == "wasif.200798":
    print("Login Successful")
else:
    print("Wrong Credential")

# and is use when we want to run the code when both condition is true and if any one became false then stop running the code

# Or Operator
choice = input("Enter q or quit to exit: ")

if choice == "q" or choice == "quit":
    print("You Quited")

# OR operator is used when we we want at least one condition to be true like it user enter q or quit the code should run

# not Operator
# not True becomes False, and not False becomes True.
is_logged_in = False

if not is_logged_in:
    print("Please log in")

#Example for Logical Operator
age = 20
has_id = False

print(age >= 18 and has_id)  # False: only one condition is true
print(age >= 18 or has_id)   # True: at least one is true
print(not has_id)            # True: reverses False


#Conditions if, else, elif
#If :
Age = 20

if age >= 18:
    print("you are an adult")

#Else :
Age1 = 15

if Age1 >= 18 :
    print("you are an adult")

else :
    print("You are under 18")

# Elif :
number = -5

if number > 0:
    print("Positive")
elif number == 0:
    print("Zero")
else:
    print("Negative")

#Loops
#For Loop
for number in range(1, 6):
    print(number)
'''
1
2
3
4
5
'''

for letter in "Wasif":
    print(letter)
'''
W
a
s
i
f
'''

number = 5

for i in range(1, 11):
    print(f"{number} × {i} = {number * i}")

#While Loop
count = 1

while count <= 5:
    print(count)
    count += 1

#Loop Control While
while True:
    choice = input("Type q to quit: ")

    if choice == "q":
        break

    print("You chose to continue")

print("Loop finished")

#Lool Control continue
for number in range(1, 6):
    if number == 3:
        continue

    print(number)


text = "  Hello Wasif  "

print(text.lower())                  # "  hello wasif  "
print(text.upper())                  # "  HELLO WASIF  "
print(text.strip())                  # "Hello Wasif"
print(text.replace("Wasif", "Python"))
print(text.split())                  # ["Hello", "Wasif"]