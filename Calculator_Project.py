import math

#Defining the operations

def add(num1, num2):
  return num1+num2
  
def subtract(num1,num2):
  return num1-num2
  
def multiply(num1,num2):
  return num1 * num2
  
def divide(num1,num2):
  return num1/num2
  
def root(num1):
  return math.sqrt(num1)
  
def factorial(num1):
  return math.factorial(num1)
  
  
  
#Number input
  
print("\t Input the numbers you want to calculate with.")

i=0 
while i == 0:

  first= int(input("First Value"))
  second= int(input("Second Value"))

#Operation input

  print("""What operation do you want?
  1 for add
  2 for subtract
  3 for multiply
  4 for divide
  5 for square root
  6 for factorial""")

  choice = input(">")
  #Adding
  if choice == "1":
    answer= add(first,second)
    print(f"{first} + {second} = {answer}")
    
  #Subtracting
  elif choice == "2":
    answer= subtract(first,second)
    print(f"{first} - {second} = {answer}")
    
  #Multiplying
  elif choice == "3":
    answer= multiply(first,second)
    print(f"{first} * {second} = {answer}")
  
  #Dividing
  elif choice == "4":
    answer= divide(first,second)
    print(f"{first} / {second} = {answer}")
  
  #Square root
  elif choice == "5":
      sqrtchoice= input("""Which value do you want to find the square root of?
      1 for first value
      2 for second value
      >""")
      if sqrtchoice == "1":
        answer= root(first)
        print(f"sqrt({first}) = {answer}")
      elif sqrtchoice == "2":
        answer= root(second)
        print(f"sqrt({second}) = {answer}")
      else: "Please pick 1 or 2."
    
  #Factorial  
  elif choice == "6":
    factchoice= input("""Which value do you want to find the factorial of?
    1 for first value
    2 for second value
    >""")
    if factchoice == "1":
      answer= factorial(first)
      print(f"{first}! = {answer}")
    elif factchoice == "2":
      answer= factorial(second)
      print(f"{second}! = {answer}")
    else: "Please pick 1 or 2."
  else: "Please choose 1,2,3,4, 5 or 6."
  
#Continue with answer?
  print("""Do you want to continue calculating with this answer?
  1 for Yes
  2 for No""")
  repeat= input(">")
  
  if repeat == "1":
    first= answer
    second= int(input("Second Value"))

    print("""What operation do you want?
  1 for add
  2 for subtract
  3 for multiply
  4 for divide
  5 for square root
  6 for factorial""")

    choice = input(">")
    if choice == "1":
      answer= add(first,second)
      print(f"{first} + {second} = {answer}")
    elif choice == "2":
      answer= subtract(first,second)
      print(f"{first} - {second} = {answer}")
    elif choice == "3":
      answer= multiply(first,second)
      print(f"{first} * {second} = {answer}")
    elif choice == "4":
      answer= divide(first,second)
      print(f"{first} / {second} = {answer}")
    elif choice == "5":
      sqrtchoice= input("""Which value do you want to find the square root of?
      1 for first value
      2 for second value
      >""")
      if sqrtchoice == "1":
        answer= root(first)
        print(f"sqrt({first}) = {answer}")
      elif sqrtchoice == "2":
        answer= root(second)
        print(f"sqrt({second}) = {answer}")
      else: "Please pick 1 or 2."
    elif choice == "6":
      factchoice= input("""Which value do you want to find the factorial of?
      1 for first value
      2 for second value
      >""")
      if factchoice == "1":
        answer= factorial(first)
        print(f"{first}! = {answer}")
      elif factchoice == "2":
        answer= factorial(second)
        print(f"{second}! = {answer}")
      else: "Please pick 1 or 2."
    
    else: "Please choose 1,2,3,4,5 or 6."
  else: "Bye."
  
  #Calculating with different numbers/loop
  print("""Do you want to calculate something else?
  1 for Yes
  2 for No""")
  again= input(">")
  if again == "1":
   print("\tInput the numbers you want to calculate with.")
  else: 
    i=i+1
    print("Bye.")
  