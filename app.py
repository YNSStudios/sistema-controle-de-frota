def veri_numero():
    while True:

        numero = input("Digite aqui: ")
        
        try:
            coversao = int(numero)
            return coversao
        except ValueError:
            print("A um erro na digitação, ou isso não é um número.")
    

veiculos = []

print("Qauntos carros você ira adicionar ?")
loop = veri_numero()
verificar = 0

while loop:

    print()
    marca = input("digite a marca do veiculo: ").capitalize()
    modelo = input("Digite do modelo do veiculo: ").capitalize()

    print("Digite o ano do veiculo: ")
    ano = veri_numero()

    veiculos.append({"marca": marca, "modelo": modelo, "ano": ano})

    verificar += 1
    if verificar == loop:
        break

for veiculo in veiculos:

    print()
    print(f"""Marca: {veiculo["marca"]}
Modelo: {veiculo["modelo"]}
Ano: {veiculo["ano"]}""")