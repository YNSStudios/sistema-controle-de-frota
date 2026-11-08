import json
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
        placa = input("Digite a placa do veiculo: ").upper()
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

    verificar += 1
    if verificar == loop:
        break

with open("veiculos.json", "w", encoding="utf-8") as autos:
    json.dump(veiculos, autos, ensure_ascii=False, indent= 4)

for veiculo in veiculos:

    marca = veiculo["marca"]
    modelo = veiculo["modelo"]
    ano = veiculo["ano"]
    responssavel = veiculo["responssavel"]
    id = veiculo["id"]

    menssagem = f"Ano: {ano}\n"
    menssagem += f"Responssavel: {responssavel}\n"
    menssagem += f"Id: {id}"

    exibiçao = Panel(menssagem, title= f"Marca: {marca}", subtitle=f"Modelo: {modelo}", width=30 )

    print()
    print(exibiçao)
    print()