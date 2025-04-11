name = ""
age = 0
earning = 0
sex1 = ""
state1 = ""

state2 = ['S', 'M', 'W', 'D']
sex2 = ['F', 'M', 'NB']

while len(name) < 3:
    name = input("Type your name: ").strip()
    if not name.replace(" ", "").isalpha():
        print("Invalid! Please Type a valid name using only letters!")
        name = ""
    else:
        print ("Confirmed")

while age <= 0 or age > 150:
    age = int(input("Type your name: "))
