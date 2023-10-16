with open('recebido.txt', 'r') as arquivo:
    # Use a função next() para ler a primeira linha
    primeira_linha = next(arquivo)
    
    # Use a função next() novamente para ler a segunda linha
    segunda_linha = next(arquivo)
x = 'ÝÝ»»ÌÌ'
bytes_hex = x.encode('utf-8').hex()
print (bytes_hex)