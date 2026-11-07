def veri_numero():
    while True:

        numero = input("Digite aqui: ")
        
        try:
            coversao = int(numero)
            return coversao
        except ValueError:
            print("A um erro na digitação, ou isso não é um número.")
    

marca = input("digite a marca do veiculo: ").capitalize()
modelo = input("Digite do modelo do veiculo: ").capitalize()

print("Digite o ano do veiculo: ")
ano = veri_numero()

print(f"""Marca: {marca}
Modelo: {modelo}
Ano: {ano}""")