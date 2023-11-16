from pprint import pprint
import re

with open('index.html', 'r', encoding='utf8') as file:
    content = file.read()

# regex to get all links
# my_regex = "href=\"(.+?)\""

# regex to get only article links
my_regex = "href=\"(.+?)\""

res = re.findall(my_regex, content)

pprint(res)