from examples import text_to_search
import re

pattern = re.compile(r"Mr\.?\s[A-Z]\w*")

finder = pattern.findall(text_to_search)
print(finder)
