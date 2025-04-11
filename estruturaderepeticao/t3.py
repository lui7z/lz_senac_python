name = ""
age = 0
earning = 0
sex1 = ""
state1 = ""

state2 = ['S', 'M', 'W', 'D']
sex2 = ['F', 'M', 'NB']

while len(name) < 2 or not name.replace(" ", "").isalpha():
    name = input("Type your name: ").strip()
    if not name.replace(" ","").isalpha():
        print("Invalid! Please type a valid name using only letters!")
        name = ""
    elif len(name) < 3:
        print("Invalid! Please type a valid name using only letters!")
        name = ""
    else:
        print ("Confirmed!")

while age <= 0 or age > 100:
    try:
        age = int(input("\nType your Age: ").strip())
        if age <= 0 or age > 100:
            print("Invalid! Please type a valid Age!")
    except ValueError:
        print("Invalid! Age must be a number!")
        age = 0
    else:
        print("Confirmed!")

while earning <= 0:
    try:
        earning = int(input("\nType your earnings: ").strip())
        if earning <= 0:
            print("Invalid! Your earnings must be Bigger than 0!")
    except ValueError:
        print("Invalid! Your earnings must be a number!")
        earning = 0
    else:
        print("Confirmed")

while sex1.upper() not in sex2:
    sex1 = input("\nType your Sex \nF - Female, M - Male, NB - Non Binary \n").strip()
    if not sex1.isalpha():
        print("Invalid! Please type one of the Options!")
        sex1 = ""
    elif sex1.upper() not in sex2:
        print("Invalid! Please type one of the Options!")
        sex1 = ""
    else:
        print ("Confirmed!")

while state1.upper() not in state2:
    state1 = input("\nType your Civic State \nS - Single, M - Married, W - Widowed, D - Divorced \n").strip()
    if not state1.isalpha():
        print("Invalid! Please type one of the Options!")
        state1 = ""
    elif state1.upper() not in state2:
        print("Invalid! Please type one of the Options!")
        state1 = ""
    else:
        print ("Confirmed!")

print(f"\nEverything that you reported was: \n{name}\n{age}\n{earning}\n{sex1}\n{state1}")