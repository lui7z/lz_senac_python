name = ""
age = 0
earning = 0
sex1 = ""
state1 = ""

state2 = ['S', 'M', 'W', 'D']
sex2 = ['F', 'M', 'NB']

while len(name) < 2 or not name.replace(" ", "").isalpha():
    name = input("Type your name: ").strip()
    if not name.replace(" ","").isalpha() or len(name) < 2:
        print("\033[31mInvalid! Please type a valid name using only letters!\033[0m")
        name = ""
    else:
        print("\033[32mConfirmed\033[0m")

while age <= 0 or age > 100:
    try:
        age = int(input("\nType your Age: ").strip())
        if age <= 0 or age > 100:
            print("\033[31mInvalid! Please type a valid Age!\033[0m")
        else:
            print("\033[32mConfirmed\033[0m")
    except ValueError:
        print("\033[31mInvalid! Age must be a number!\033[0m")
        age = 0

while earning <= 0:
    try:
        earning = int(input("\nType your earnings: ").strip())
        if earning <= 0:
            print("\033[31mInvalid! Your earnings must be Bigger than 0!\033[0m")
        else:
            print("\033[32mConfirmed\033[0m")
    except ValueError:
        print("\033[31mInvalid! Your earnings must be a number!\033[0m")
        earning = 0

while sex1.upper() not in sex2:
    sex1 = input("\nType your Sex \nF - Female, M - Male, NB - Non Binary \n").strip().upper()
    if not sex1.isalpha() or sex1 not in sex2:
        print("\033[31mInvalid! Please type one of the Options!\033[0m")
        sex1 = ""
    else:
        print("\033[32mConfirmed\033[0m")

while state1.upper() not in state2:
    state1 = input("\nType your Civic State \nS - Single, M - Married, W - Widowed, D - Divorced \n").strip().upper()
    if not state1.isalpha() or state1 not in state2:
        print("\033[31mInvalid! Please type one of the Options!\033[0m")
        state1 = ""
    else:
        print("\033[32mConfirmed\033[0m")

print(f"\nEverything that you reported was: \nName: \033[32m{name}\033[0m\nAge: \033[32m{age}\033[0m\nEarnings: \033[32m{earning}\033[0m\nSex: \033[32m{sex1}\033[0m\nCivic State: \033[32m{state1}\033[0m")