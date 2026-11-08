import json
import re
from random import randint
from rich import print
from rich.panel import Panel

try:
    with open("veiculos.json", "r", encoding="utf-8") as autos:
        veiculos = json.load(autos)
except FileNotFoundError:
    veiculos = []
 

def Veri_numero():
    while True:

        numero = input("Digite aqui: ")
        
        try:
            coversao = int(numero)
            return coversao
        except ValueError:
            print("[red]A um erro na digitação, ou isso não é um número.[/]")


def Id():
    while True:
        id = randint(10001, 999999)

        id_copia = None

        for veiculo in veiculos:
            if veiculo["id"] == id:
                id_copia = veiculo
                break

        if id_copia is None:
            return id
    

def Veri_placa():
    while True:
        while True:
            placa = input("Digite a placa do veiculo: ").upper().strip()
            if re.search(r"^[A-Z]{3}[0-9][A-Z][0-9]{2}$|^[A-Z]{3}-?[0-9]{4}$", placa):
                break
            else:
                print("A placa não segue o fomato.")

        placa_copia = None

        for veiculo in veiculos:
            if placa == veiculo["placa"]:
                placa_copia = veiculo
                print("[red]A placa já existe e não pode ser usada.[/]")
                break

        if placa_copia is None:
            return placa


print("Qauntos carros você ira adicionar ?")
loop = Veri_numero()
verificar = 0

atual = []

while loop:

    print()
    responssavel = input("Digite o nome completo do responssavel do veiculo. (Motorista ou Dono): ").title()
    marca = input("digite a marca do veiculo: ").capitalize()
    modelo = input("Digite do modelo do veiculo: ").capitalize()
    placa = Veri_placa()
    id = Id()

    print("Digite o ano do veiculo: ")
    ano = Veri_numero()

    veiculos.append({"responssavel": responssavel, "marca": marca, "modelo": modelo, "ano": ano, "placa": placa, "id": id})
    atual.append({"responssavel": responssavel, "marca": marca, "modelo": modelo, "ano": ano, "placa": placa, "id": id})

    verificar += 1
    if verificar == loop:
        break

for veiculo in atual:

    marca = veiculo["marca"]
    modelo = veiculo["modelo"]
    ano = veiculo["ano"]
    responssavel = veiculo["responssavel"]
    id = veiculo["id"]
    placa = veiculo["placa"]

    menssagem = f"Ano: {ano}\n"
    menssagem += f"Responssavel: {responssavel}\n"
    menssagem += f"Placa: {placa}\n"
    menssagem += f"Id: {id}"

    exibiçao = Panel(menssagem, title= f"Marca: {marca}", subtitle=f"Modelo: {modelo}", width=30, border_style="yellow", style= "orange3" )

    print()
    print(exibiçao)
    print()

with open("veiculos.json", "w", encoding="utf-8") as autos:
    json.dump(veiculos, autos, ensure_ascii=False, indent= 4)