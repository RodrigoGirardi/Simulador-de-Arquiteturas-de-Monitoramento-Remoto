import csv #Com essa biblioteca ele faz as divisões automáticamente nas virgulas 

# Abre o arquivo CSV em modo de leitura ('r')
with open('teste.csv', 'r', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)

    # Itera pelas linhas do arquivo CSV
    for linha in leitor_csv:
        # Cada linha é uma lista contendo os valores das colunas
        nome = linha[0]
        idade = linha[1]  # Converte a idade para inteiro
        cidade = linha[2]

        print(f"Nome: {nome}, Idade: {idade}, Cidade: {cidade}")