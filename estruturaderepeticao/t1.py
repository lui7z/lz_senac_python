note = int(input("Type a note between 0 and 10: "))

while note < 0 or note > 10:
    print("invalid")
    note = int(input("Type a valid note: "))

print("ok")