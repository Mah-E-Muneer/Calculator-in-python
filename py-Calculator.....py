print ("CALULATOR")

num1 = int(input(" enter first number:" ))
num2 = int(input(" enter second number:" ))

##print("press 1 for addition, press 2 for subtraction, press 3 for multiplication, press 4 for division")

choice = int(input("enter your choicefrom 1-4: "))

if choice ==1:
   print (num1 + num2)
elif choice ==2:
   print (num1 - num2)
elif choice ==3:
   print (num1 * num2)
elif choice ==4:
   print (num1 / num2)
else:
   print ("Invalid Input")
                    
