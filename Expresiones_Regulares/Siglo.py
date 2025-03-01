import re
from sys import stdin, stdout

text = stdin.readline()
pattern = r"\b\d{4}\b"
results = re.findall(pattern, text)
for match in results:
    stdout.write(match + '\n')
