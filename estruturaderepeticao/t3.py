name = str(input("Type your Name: \n"))
age = int(input("Type your Age: \n"))
earning = float(input("Type your Earnings: \n"))
sex = str(input("Type your Sex: \nF - Female, M - Male")).upper()
state = str(input("Type your Civil State: \n"))



while age < 0 and age > 150:
    print("Invalid Age")
    age = int(input("Type your Age: \n"))

while earning < 0:
    print("Invalid Earning")
    earning = float(input("Type your Earnings: \n"))



print("Everything Ok!")