phrases = ("I love you", "a little", "a lot", "passionately", "madly", "not at all")
try:
    petals = int(input("Enter the amount of petals: "))
    if petals > 0:
        last_phrase = (petals % len(phrases)) - 1
        print(f"Last phrase is '{phrases[last_phrase]}'")
    else:
        print("Number must be higher than 0.")
except ValueError:
    print("You have to enter integer number.")
