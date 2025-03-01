from sys import stdin, stdout
import re

text = stdin.readline().strip()
pattern_alumno = r"\b([a-z])\.([a-z]{2,})\.(\d{4})@alumnos\.urjc\.es\b"
pattern_profe = r"\b([a-z]{1,})\.([a-z]{1,})@urjc\.es\b"
results_alumno = re.findall(pattern_alumno, text)
results_profe = re.findall(pattern_profe, text)
for match in results_alumno:
    inicial, apellido, ano = match
    stdout.write(f"alumno {apellido} matriculado en {ano}\n")

for match in results_profe:
    nombre, apellido = match
    stdout.write(f"profesor {nombre} apellido {apellido}\n")

