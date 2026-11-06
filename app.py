import json
from rich import print
from rich.panel import Panel

try:
    with open("veiculos.json", 'r', encoding='utf-8') as autos:
        veiculos = json.load(autos)

except FileExistsError:
    veiculos = []

