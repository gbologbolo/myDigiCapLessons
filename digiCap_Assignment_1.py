print("This programme will ask you for a number and print out the Time Table of that number (i.e. from 1 to 12)")
print("NOTE: Please only whole numbers are allowed")
user_number = float(input("Input any number you want "))
user_number = int(user_number)
print("Time Table of "+ str(user_number) + " is as follows")
times = int("1")
while (times <= 12):
    answer = user_number * times
    answer = int(answer)
    print(str(user_number) + " by " + str(times) + " = " + str(answer))
    times = times+1
else:
    print("Thank you!")