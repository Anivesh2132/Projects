# # # # i = input("add first no:")
# # # # j = input("add second no:")

# # # # add = (int(i) + int(j))
# # # # print("x+y=",add)
# # # # minus = (int(i) - int(j))
# # # # print("x-y=",minus)

# num1 = float(input("Enter the 1st num: "))
# num2 = float(input("Enter the 2nd num: "))
# operator = input("Enter an operator (+,-, *, /):")
            

# if operator == "+":
#     result = num1 + num2
#     print(round(result))
    
# elif operator == "-":
#     result = num1 - num2
#     print(round(result))
    
# elif operator == "*":
#     result = num1 * num2 
#     print(round(result))
       
# elif operator == "/":
#     result = num1 / num2

#     print(round(result))
    
# else:
#     print("not a valid operator")




def add(P, Q):    
   # This function is used for adding two numbers   
   return P + Q   
def subtract(P, Q):   
   # This function is used for subtracting two numbers   
   return P - Q   
def multiply(P, Q):   
   # This function is used for multiplying two numbers   
   return P * Q   
def divide(P, Q):   
   # This function is used for dividing two numbers    
   return P / Q    
# Now we will take inputs from the user    
print ("Please select the operation.")    
print ("a. Add")    
print ("b. Subtract")    
print ("c. Multiply")    
print ("d. Divide")    
    
choice = input("Please enter choice (a/ b/ c/ d): ")    
    
num_1 = int (input ("Please enter the first number: "))    
num_2 = int (input ("Please enter the second number: "))    
    
if choice == 'a':    
   print (num_1,"+ ", num_2, " = ", add(num_1, num_2))    
    
elif choice == 'b':    
   print (num_1,"- ", num_2, " = ", subtract(num_1, num_2))    
    
elif choice == 'c':    
   print (num_1," * ", num_2, " = ", multiply(num_1, num_2))    
elif choice == 'd':    
   print (num_1,"/ ", num_2, " = ", divide(num_1, num_2))    
else:    
   print ("This is an invalid input")    





# # Import 'math' and 'random' Libraries
# import math
# import random
# # Define Variables
# output = 0
# num1 = ""
# operator = ""
# num2 = ""
# memStore = "Empty"

# # Define Function Listing Function
# def abilitiesList():
#     print("+...Addition")
#     print("-...Subtraction")
#     print("*...Multiplication")
#     print("/...Division")
#     print("^...Powers")
#     print("/-...Square Roots ")
#     print("!...Factorials (Input Cannot Be Negetave)")
#     print("Abs...Absolute Value")
#     print("d/r...Degrees To Radians")
#     print("r/d...Radians To Degrees")
#     print("pi...Returns PI")
#     print("e...Returs 'e'")
#     print("tau...Returns TAU (2xPI)")
#     print("M+...Save input to memory")
#     print("MR...Recall Memory")
#     print("M-...Clear Memory")
#     print("sin...Sine")
#     print("cos...Cosine")
#     print("tan...Tangent")
#     print("asin...Arc Sine")
#     print("acos...Arc Cosine")
#     print("atan...Arc Tangent")
#     print("log10...Log(10) of Input")
#     print("log...Returns The Apropriate Log of the Input (input1 is the log power)")
#     print("rand...Returns A Random Number Between 0 and 1")
#     print("randint...Returns A Random Number Between The Two Inputs")
#     print("//////////////////////////////////////////////////////////////////////////")

# def askForNumInput(textPrompt):
#     # Devine local variable
#     convertedNum = math.nan

#     # Wait for valid numerical input 
#     while True:
#         num = input(textPrompt)
#         try:
#             # Try to typecast the input to a float
#             float(num)
#         except ValueError:
#             # Catch the exception if it is not a number
#             print("ERROR: Syn: Invalid Num")
#         else:
#             # Typecasting
#             convertedNum = float(num)
#             break
#     return convertedNum

# # While Loop
# while True:
#     print("//////////////////////////////////////////////////////////////////////////")
#     print("Type 'help' for a list of abilities")
#     # Loop for getting operation
#     while True:
#         operator = input("What operation do you want to perform? ")
#         # Is operator == to any of out constants or predefines?
#         if operator == "help":
#             abilitiesList()
#         elif operator == "pi":
#             print(math.pi)
#         elif operator == "e":
#             print(math.e)
#         elif operator == "tau":
#             print(math.pi*2)
#         elif operator == "MR":
#             print(str(memStore))
#         elif operator == "M-":
#             memStore = "Empty"
#             print("Memory Cleared")
#         elif operator == "rand":
#             print(random.random())
#         # Has the user entered in a valid operator?
#         elif operator == "+" or operator == "-" or operator == "*" or operator == "/" or operator == "^" or operator == "/-" or operator == "!" or operator == "Abs" or operator == "d/r" or operator == "r/d" or operator == "M+" or operator == "M-" or operator == "MR" or operator == "sin" or operator == "cos" or operator == "tan" or operator == "asin" or operator == "acos" or operator == "atan" or operator == "log10" or operator == "log" or operator == "randint":
#             break
#         else:
#             print("ERROR: Invalid Operator")

#     # Loop for 1st number input
#     while True:
#         num1 = askForNumInput("First Number? ")
#         # Catch asin and acos out of bounds error case
#         if (operator == "asin" or operator == "acos") and (num1 > 1 or num1 < -1):
#             print("ERROR: Math: 'asin' and 'acos' commands only accept inputs in range -1 to +1")
#         elif operator == "!" and num1 < 0:
#             print("ERROR: Math: Factorials only accept inputs > 0")
#         else:
#             break

#     # Does the operation require a 2nd input?
#     if not (operator=="/-" or operator=="!" or operator=="Abs" or operator=="d/r" or operator=="r/d" or operator=="M+" or operator=="sin" or operator=="cos" or operator=="tan" or operator=="asin" or operator=="acos" or operator=="atan" or operator=="log10"):
#         # Loop for 2nd number input
#         while True:
#             num2 = askForNumInput("Second Number? ")
#             # Catch x/0 error case
#             if  operator == "/" and num2 == "0":
#                 print("ERROR: Math: Canot divide by 0!")
#             else:
#                 break

#     # Calculations
#     if operator == "+":
#         output = num1 + num2
#         print("Your Answer: "+str(output))
#     elif operator == "-":
#         output = num1 - num2
#         print("Your Answer: "+str(output))
#     elif operator == "*":
#         output = num1 * num2
#         print("Your Answer: "+str(output))
#     elif operator == "/":
#         output = num1 / num2
#         print("Your Answer: "+str(output))
#     elif operator == "^":
#         output = math.pow(num1,num2)
#         print("Your Answer: "+str(output))
#     elif operator == "/-":
#         output = math.sqrt(num1)
#         print("Your Answer: "+str(output))
#     elif operator == "!":
#         output = math.factorial(num1)
#         print("Your Answer: "+str(output))
#     elif operator == "Abs":
#         output = math.fabs(num1)
#         print("Your Answer: "+str(output))
#     elif operator == "d/r":
#         output = math.radians(num1)
#         print("Your Answer: "+str(output))
#     elif operator == "r/d":
#         output = math.degrees(num1)
#         print("Your Answer: "+str(output))
#     elif operator == "M+":
#         memStore = num1
#         print("Number Stored")
#     elif operator == "sin":
#         output = math.sin(num1)
#         print("Your Answer: "+str(output))
#     elif operator == "cos":
#         output = math.cos(num1)
#         print("Your Answer: "+str(output))
#     elif operator == "tan":
#         output = math.tan(num1)
#         print("Your Answer: "+str(output))
#     elif operator == "asin":
#         output = math.asin(num1)
#         print("Your Answer: "+str(output))
#     elif operator == "acos":
#         output = math.acos(num1)
#         print("Your Answer: "+str(output))
#     elif operator == "atan":
#         output = math.atan(num1)
#         print("Your Answer: "+str(output))
#     elif operator == "log10":
#         output = math.log10(num1)
#         print("Your Answer: "+str(output))
#     elif operator == "log":
#         output = math.log(num2, num1)
#         print("Your Answer: "+str(output))
#     elif operator == "randint":
#         output = random.randint(num1, num2)
#         print("Your Answer: "+str(output))

