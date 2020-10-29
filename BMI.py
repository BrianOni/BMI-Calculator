#Brian Onieal
#Question 5

height=float(input("Please input your height in inches: "))  #Height in inches
weight=float(input("Please input your weight in pounds: "))  #Weight in pounds

BMI = weight* 703/height**2     #Calculating the BMI

if BMI <18.5:                      #If BMI is less than 18.5, underweight
    print("You are underweight")
elif BMI <=25:
    print("You are just right")    #If BMI is betweek 18.5 and 25, just right
elif BMI >=25:
    print("You are overweight")    #If BMI is over 25, overweight

