import re
from sys import stdin, stdout

text = stdin.readline().strip()
pattern = r"\b(\d{4})-(\d{2})-(\d{2})\b"
pattern_sustituicion = r"\3.\2.\1"
text_sustituido = re.sub(pattern, pattern_sustituicion, text)
stdout.write(text_sustituido + "\n")

