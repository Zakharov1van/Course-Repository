import re

pattern = re.compile(r"[89]00-\d+-\d+")

with open("data.txt", "r") as data_file:
    content = data_file.read()
    finder = pattern.findall(content)
    print(finder)
