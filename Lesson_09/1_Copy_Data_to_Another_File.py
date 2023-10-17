with open("text_1.txt", "r") as file:
    with open("text_2.txt", "w") as new_file:
        for line in file:
            new_file.write(line)
