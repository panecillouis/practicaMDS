import re
from sys import stdin, stdout


text = stdin.readline().strip()
pattern = (r'\b(?:C\/|Calle)\s([A-ZÁÉÍÓÚÜÑ][a-zA-ZáéíóúüñÁÉÍÓÚÜÑ/\'-]+)[,]?\s+(?:N|n|Nº|nº|N |n |Nº |nº )?(\d{1,2}),'
           r'\s+(\d{5})\b')

resultado = re.findall(pattern, text)

for match in resultado:
    calle, numero, codigo = match
    stdout.write(f"{codigo}-{calle}-{numero}\n")
