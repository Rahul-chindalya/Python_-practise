#You are building a simple OTP (One-Time Password) verification system. The user will be asked to enter a 4-digit OTP. They will be given 3 attempts to enter the correct OTP.
#Assume the correct OTP is already stored in a variable.
#Ask the user to input a 4-digit OTP.
#If the OTP entered is not 4 digits, display
#OTP Must be 4 digit number only
#If the OTP is correct, display:
#Correct OTP - Success
#If the OTP is incorrect, decrease the attempts count.
#After 3 incorrect attempts, display
#Maximum attempts done, try after 24 Hours

import random

otp=random.randint(1000,9999)

print(otp)

count = 3

while count>0:
    user_otp = int(input("Enter otp: "))

    if len(str(user_otp))!=4:
        print("opt must be in 4 digit")
    if user_otp==otp:
        print("correct otp")
        break
    count-=1
else :
    print("max attempt done,try after 24hr")
