import re
from sys import stdin, stdout

text = stdin.readline().strip()
pattern = (r"\b\d{4}-\d{2}-\d{2}\s\d{2}:\d{2}:\d{2}\.\d{3}\s+([A-Z]\w+)\s+\d+\s+---\s+\[(.*?)\]\s+([\w\d\.]+)\s+:\s+("
           r".+)")

resultado = re.findall(pattern, text)

for match in resultado:
    nivel, hilo, clase, mensaje = match
    clase = clase.split(".")[-1]
    mensaje = mensaje.strip().replace('"', '""')
    stdout.write(f'"{nivel}","{hilo}","{clase}","{mensaje}"\n')
