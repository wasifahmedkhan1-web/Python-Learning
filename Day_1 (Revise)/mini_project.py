Name = input("What is your name? ")

while True:
    Software = input("Which Software you want to run (lowercase): ")
    
    if Software.lower() == "calculator":
        print("Hey,", Name, "Welcome to the Calculator")
        print("Made by Wasif")
        print("This Calculator Only support +, -, *, /")
        
        while True:
            First_Number = float(input("Please enter First Number: "))
            Second_Number = float(input("Please enter Second Number: "))
            Operation = input("Enter the Operation you want to conduct: ")
            
            if Operation == "+":
                print("Addition of the Numbers = ", First_Number + Second_Number)
            elif Operation == "-":
                print("Substraction of the Numbers = ", First_Number - Second_Number)
            elif Operation == "*":
                print("Multiplication of the numbers = ", First_Number * Second_Number)
            elif Operation == "/":
                if Second_Number == 0:
                    print("You can not divide a number by zero because answer is infinity")
                else:
                    print("When number first divided by second number = ", First_Number / Second_Number)
            else:
                print("Invalid operation")
                
            Quiting = input("Enter 'q' to Quit, or press ENTER to calculate again: ")
            if Quiting.lower() == "q":
                print("Calculator closed")
                break
        break  
        
    else:
        print("That Software Source Code is Not Available")
        print("Contract Wasif for further Assistance")
        print("Email : wasifahmedkhan1@gmail.com")