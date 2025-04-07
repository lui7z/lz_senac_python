vowel = ['a', 'e', 'i', 'o', 'u']
consonant = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'x', 'y', 'z']

letter = input("Type a Letter: ")

if letter.lower() in vowel:
    print("The letter", letter, "is a Vowel!")
elif letter.lower() in consonant:
    print("The letter", letter, "is a Consonant!")
else:
    print("That isn't a letter!")