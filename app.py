import json
import re
from time import sleep
from random import randint
from rich import print
from rich.panel import Panel

try:
    with open("veiculos.json", "r", encoding="utf-8") as autos:
        veiculos = json.load(autos)
except FileNotFoundError:
    veiculos = []

atual = []
 

def Veri_numero():
    while True:

        numero = input("Digite aqui: ").strip()
        
        try:
            conversao = int(numero)
            if conversao >= 1:
                return conversao   
            else:
                print("O valor deve ser maior que 0.") 
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
            placa.replace("-", "")
            if re.search(r"^[A-Z]{3}[0-9][A-Z][0-9]{2}$|^[A-Z]{3}[0-9]{4}$", placa):
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


titulo = "Sistema de gerenciamento de frota."
menu = Panel(titulo, title="Menu", style="white", border_style="yellow", width=30)
print(menu)

opçoes = "[1] Criar/adicionar veiculo.\n[2] Editar veiculo\n[3] Remover veiculo.\n[4] Pesquisar veiculo.\n[5] Sair"
menu0 = Panel(opçoes, title="Opções", border_style="yellow", width=30)
print(menu0)

while True:

    escolha = Veri_numero()

    if escolha == 1:

        print("Criação")

        print("Quantos carros você ira adicionar ?")
        loop = Veri_numero()
        verificar = 0

        while loop:

            print()
            responssavel = input("Digite o nome completo do responssavel do veiculo. (Motorista ou Dono): ").strip().title()
            marca = input("digite a marca do veiculo: ").strip().capitalize()
            modelo = input("Digite do modelo do veiculo: ").strip().capitalize()
            placa = Veri_placa()
            id = Id()

            print("Digite o ano do veiculo: ")
            ano = Veri_numero()

            veiculos.append({"responssavel": responssavel, "marca": marca, "modelo": modelo, "ano": ano, "placa": placa, "id": id})
            atual.append({"responssavel": responssavel, "marca": marca, "modelo": modelo, "ano": ano, "placa": placa, "id": id})

            
            with open("veiculos.json", "w", encoding="utf-8") as autos:
                json.dump(veiculos, autos, ensure_ascii=False, indent= 4)

            verificar += 1
            if verificar == loop:
                break

        print(atual)

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

    elif escolha == 2: 

        print("Edição")

        while True:

            busca = input("Digite o id do veiculo ou nome do responssavel: ").strip().title()
            print()

            if busca.isnumeric():

                encontrado = None

                for veiculo in veiculos:
                    if  veiculo["id"] == busca:
                        encontrado = veiculo
                        break

            elif busca.isalpha:

                encontrado = None

                for veiculo in veiculos:
                    if veiculo["responssavel"] == busca:
                        encontrado = veiculo
                        break

            if encontrado is not None:
                break
            else:
                print("[red]Não encontrado[/]")

        marca = encontrado["marca"]
        modelo = encontrado["modelo"]
        ano = encontrado["ano"]
        responssavel = encontrado["responssavel"]
        id = encontrado["id"] 
        placa = encontrado["placa"]

        menssagem = f"Ano: {ano}\n"
        menssagem += f"Responssavel: {responssavel}\n"
        menssagem += f"Placa: {placa}\n"
        menssagem += f"Id: {id}"

        exibiçao = Panel(menssagem, title= f"Marca: {marca}", subtitle=f"Modelo: {modelo}", width=30, border_style="yellow", style= "orange3" )

        print()
        print(exibiçao)
        print()
        
        painel_editar = "[1] Marca/Modelo\n[2] Responssavel"

        exibiçao_editar = Panel(painel_editar, title="Edição", border_style="yellow", style="orange3", width=30)

        print(exibiçao_editar)
        print()

        while True:

            print("Digite sua escolha. ")
            escolha1 = Veri_numero()

            if escolha1 == 1:

                marca = encontrado["marca"]
                modelo = encontrado["modelo"]

                caixa = f"Marca: {marca}\nModelo: {modelo}"
                exibiçao_caixa = Panel(caixa, title="Qual ira editar ?", width=30)
                print(exibiçao_caixa)

                while True:

                    editar_escolha = input("Qual vai editar: ").strip().lower()

                    if editar_escolha == "modelo" or encontrado['marca']:

                        encontrado["modelo"] = input("Digite o novo modelo: ")
                        print("Digite o ano.")
                        encontrado["ano"] = Veri_numero()
                        print("Digite a placa.")
                        encontrado["placa"] = Veri_placa()
                        encontrado["id"] = Id()

                    elif editar_escolha == "marca" or encontrado['modelo']:

                        encontrado["marca"] = input("Digite a marca do novo veiculo: ")
                        encontrado["modelo"] = input("Digite o modelo: ")
                        print("Digite o ano.")
                        encontrado["ano"] = Veri_numero()
                        print("Digite a placa.")
                        encontrado["placa"] = Veri_placa()
                        encontrado["id"] = Id()
                        
                    with open("veiculos.json", "w", encoding="utf-8") as autos:
                        json.dump(veiculos, autos, ensure_ascii=False, indent=4) 
                    atual.append(encontrado)

                    atual.append({"responssavel": encontrado["responssavel"], "marca": encontrado['marca'], "modelo": encontrado["modelo"], "ano": encontrado["ano"], "placa": encontrado['placa'], "id": encontrado["id"]})
                    
                    for veiculo in atual:

                        marca = veiculo["marca"]
                        modelo = veiculo["modelo"]
                        ano = veiculo["ano"]
                        responssavel = veiculo["responssavel"]
                        id = veiculo["id"]
                        placa = veiculo["placa"]

                        menssagem = f'Ano: {ano}\n'
                        menssagem += f"Responssavel: {responssavel}\n"
                        menssagem += f"Placa: {placa}\n"
                        menssagem += f"Id: {id}"

                        exibiçao = Panel(menssagem, title= f"Marca: {marca}", subtitle=f"Modelo: {modelo}", width=30, border_style="yellow", style= "orange3" )

                        print()
                        print(exibiçao)
                        print()            

    elif escolha == 3:

        print("Exclusão")

        while True:
        
            while True:

                busca = input("Digite o id do veiculo ou nome do responssavel: ").strip().title()

                if busca.isnumeric():

                    encontrado = None

                    for veiculo in veiculos:
                        if  veiculo["id"] == busca:
                            encontrado = veiculo
                            break

                elif busca.isalpha:

                    encontrado = None

                    for veiculo in veiculos:
                        if veiculo["responssavel"] == busca:
                            encontrado = veiculo
                            break

                if encontrado is not None:
                    break
                else:
                    print("[red]Não encontrado[/]")

            marca = encontrado["marca"]
            modelo = encontrado["modelo"]
            ano = encontrado["ano"]
            responssavel = encontrado["responssavel"]
            id = encontrado["id"] 
            placa = encontrado["placa"]

            menssagem = f"Ano: {ano}\n"
            menssagem += f"Responssavel: {responssavel}\n"
            menssagem += f"Placa: {placa}\n"
            menssagem += f"Id: {id}"

            exibiçao = Panel(menssagem, title= f"Marca: {marca}", subtitle=f"Modelo: {modelo}", width=30, border_style="yellow", style= "orange3" )

            print()
            print(exibiçao)
            print()

            comfirmação = input("Está correto ? (Sim ou não): ").strip().lower()

            if comfirmação == "sim":

                veiculos.remove(encontrado)

                with open("veiculos.json", "w", encoding="utf-8") as autos:
                    json.dump(veiculos, autos, ensure_ascii=False, indent=4)

                print("Removido com sucesso.")
                print(menu0)
                break

            elif comfirmação == "não" or "nao":

                print("Reiniciando")
                sleep(0.6)
                print("Preparando tudo")
                sleep(0.6)
                print("Esvaziando lista")

    elif escolha == 4:

        print("Pesquisar")

        while True:

            busca = input("Digite o id do veiculo ou nome do responssavel: ").strip().title()
            print()

            if busca.isnumeric():

                encontrado = None

                for veiculo in veiculos:
                    if  veiculo["id"] == busca:
                        encontrado = veiculo
                        break

            elif busca.isalpha:

                encontrado = None

                for veiculo in veiculos:
                    if veiculo["responssavel"] == busca:
                        encontrado = veiculo
                        break

            if encontrado is not None:
                break
            else:
                print("[red]Não encontrado[/]")

        marca = encontrado["marca"]
        modelo = encontrado["modelo"]
        ano = encontrado["ano"]
        responssavel = encontrado["responssavel"]
        id = encontrado["id"] 
        placa = encontrado["placa"]

        menssagem = f"Ano: {ano}\n"
        menssagem += f"Responssavel: {responssavel}\n"
        menssagem += f"Placa: {placa}\n"
        menssagem += f"Id: {id}"

        exibiçao = Panel(menssagem, title= f"Marca: {marca}", subtitle=f"Modelo: {modelo}", width=30, border_style="yellow", style= "orange3" )

        print()
        print(exibiçao)
        print() 

        print(menu0)

    elif escolha == 5:
        break