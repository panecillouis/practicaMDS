import re
from sys import stdin, stdout

text = stdin.readline()
pattern = r"\b(?:E[- ]?)?\d{4}[- ]?[A-Z]{3}\b"
results = re.findall(pattern, text)
for match in results:
    stdout.write(match + '\n')
