#information about the programme for the user
print("This programme will ask you for a number and print out the Time Table of that number (i.e. from 1 to 12)")
print("NOTE: Please only whole numbers are allowed")

#Asking the User for an input number
user_number = float(input("Input any number you want: "))

#Converting floating numbers to integer numbers
user_number = int(user_number)

print("Times Table of ["+ str(user_number) + "] is as follows")

#Initialization of the starting point of the times table (from 1 to 12)
times = int("1")

#Condition for the iteration...
while (times <= 12):
    #performing arthematics
    answer = user_number * times
    
    #displaying the times table of the user input number
    print(str(user_number) + " by " + str(times) + " = " + str(answer))

    #Increamenting the initiazation value
    times = times+1
else:
    print("Thank you!")
