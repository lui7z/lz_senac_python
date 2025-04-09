shift = input("Which shift do you study? \nType 'M' for Morning, 'V' for Evening and 'N' for Nocturnal\n").upper()

if shift == 'M':
    print("Good Morning!")
elif shift == 'V':
    print("Good Afternoon!")
elif shift == 'N':
    print("Good Night!")
else:
    print("That not an valid Shift!")