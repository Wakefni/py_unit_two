#Nicholas Wakefield
#10/2/23
#Chatbot that helps you with car payments
userName = input("Hello! My name is ChatBot0.32, what's yours?: ")
print("Hello",userName,"it's nice to meet you!")
userLocation = input("Where are you from?: ")
#did some messing around with if-else statements just for fun :)
if userLocation in ("Maryland"):
    print("Wow! Why would you live in a place like that?")
else:
    print("Wow!",userLocation,"sounds nice!")
userNumber = input("Just curious, what's your favorite number?: ")
controllerNumber = 7
outputNumber = (int(userNumber)-7)
print("Your favorite number",userNumber,"is",outputNumber,"greater than my favorite number!")
userCar = input("What is your dream car {}?: ".format(userName))
#Another if-else statement
if userCar in ("Edsel"):
    print("Know your car history huh?")
    carCost = input("How much does a junkheap like that cost?: ")
else:
    carCost = input("Wow! I always wanted a {} too! How much does it cost?: ".format(userCar))
annualInterestRate = input("What is the annual interest rate for a car loan?: ")
loanYears = input("And if you had to take out a loan to buy the {}, how many years would you take the loan out for?: ".format(userCar))
monthlyInterestRate = (float(annualInterestRate)/100)/12
monthlyPayment = (float(monthlyInterestRate)*float(carCost))/(1-(1+float(monthlyInterestRate))**(-1*(float(loanYears)*12)))
fullCost = (float(monthlyPayment)*(float(loanYears)*12))
fullCostTrue = round(fullCost,2)
monthlyPaymentTrue = round(monthlyPayment,2)
print("Your monthly payment for the",userCar,"is",monthlyPaymentTrue,"$ that is a total of",fullCostTrue,"$!")
print("Goodbye",userName,"I hope you found this helpful!")


