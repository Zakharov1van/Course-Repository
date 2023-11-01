from examples import urls
import re

pattern = re.compile(r"https?://(www\.)?(\w+)(\.\w+)")
finder = pattern.finditer(urls)
for element in finder:
    print(element.group())

changed_str = pattern.sub(r"\2\3", urls)
print(changed_str)
