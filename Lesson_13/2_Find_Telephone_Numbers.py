from examples import text_to_search
import re

pattern = re.compile(r"\d+-\d+-\d+")
finder = pattern.findall(text_to_search)
print(finder)
