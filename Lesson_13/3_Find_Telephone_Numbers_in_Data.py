import re

pattern = re.compile(r"\d+-\d+-\d+")

with open("data.txt", "r") as data_file:
    content = data_file.read()
    finder = pattern.findall(content)
    print(finder)
