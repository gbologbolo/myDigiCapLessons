number = float(input("Input any number you want "))
num = int("1")

#Condition for the iteration...

if number.is_integer():
    while (num < 13):
        #performing arthematics
        number = int(number)
        answer = number * num
        answer = int(answer)
        #displaying the times table of the user input number
        print(str(num) + " x " + str(number) + " = " + str(answer))
        
        #Increamenting the initiazation value
        num = num+1
elif(num<13):
    while (num<13):
        number = int(number)
        #performing arthematics
        answer = number * num
        answer = int(answer)    
        #displaying the times table of the user input number
        print(str(num) + " x " + str(number) + " = " + str(answer))
            
        #Increamenting the initiazation value
        num = num+1
    else:
        print("Thank you")
else: 
     print("Your input is not an integer")
