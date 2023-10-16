import csv #Com essa biblioteca ele faz as divisões automáticamente nas virgulas 
#############################################
####   Funcoes de converção de binário   ####
#############################################
def convert_cmd(cmd_b):
    decimal_cmd = int(cmd_b, 2)
    return decimal_cmd

def convert_size(size_b):
    decimal_size = int(size_b, 2)
    return decimal_size

def convert_data(data_b):
    decimal_data = int(data_b, 2)
    return decimal_data

def convert_crc1(crc1):
    decimal_crc1 = int(crc1, 2)
    return decimal_crc1
# Abre o arquivo CSV em modo de leitura ('r')

data = []

with open('data.csv', 'r', newline='') as arquivo_csv:
    leitor_csv = csv.reader(arquivo_csv)
    for linha in leitor_csv:
        cmd = linha[0]
        size = linha[1]

        for size in linha:
            data.append(size)
        crc1 = data[len(data)-1]
        data = data[2:]
        data.pop(-1)
        #print(f"Comando = {cmd}, Size: {size}, Dados: {data}, CRC: {crc1}")  #Exemplo: 02,09,01,02,AA,AA,BB,BB,CC,CC,05    

        crc = 0

        #cmd = int(cmd)
        #size = int(size)

        print(f"Resultado: {crc}")
        crc = (crc) ^ (cmd)
        print(f"Resultado: {crc}")
        crc = (crc) ^ (size)
        print(f"Resultado: {crc}")
        crc = (crc) ^ (data)
        print(f"Resultado: {crc}")
        if(crc == crc1):
            print(f"Dados consistentes.")
        else:
            print(f"Erro de verificação.")
            
        data.clear()
'''
**tamanho-função**
******************
    8bits-cmd
    8bits-size
    size-data
    8bits-crc1
    8bits-crc2
'''

'''        decimal_cmd = convert_cmd(cmd)
        decimal_size = convert_size(size)
        decimal_data = convert_data(data)
        decimal_crc1 = convert_data(crc1)


        if decimal_cmd is not None:    
            if decimal_size is not None:
                if decimal_data is not None:
                    if decimal_crc1 is not None:
                            print(f"Comando = {decimal_cmd}, Size: {decimal_size}, Dados: {decimal_data}, CRC1: {decimal_crc1}")
                    else:
                        print(f"Valor inválido para CRC1: {crc1}")
                else:
                    print(f"Valor inválido para Data: {data}")
            else:
                print(f"Valor inválido para Size: {size}")
        else:
            print(f"Valor inválido para Comando: {cmd}")'''
