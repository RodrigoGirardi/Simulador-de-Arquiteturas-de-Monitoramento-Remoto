import socket
import threading
import time
from typing import Deque, Any
from collections import deque
import queue ###   https://www.guru99.com/python-queue-example.html
from colorama import Fore, Back, Style, init


MAX_SIZE_BUFFER = 2000
init(autoreset=True)
fifo = queue.Queue()

################### SERVIDOR
def servidor():
    HOST = '10.32.162.132'
    PORT = 5555
    recebe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    recebe.bind(('10.32.162.132', 5555))
    recebe.listen(1)
    print('Aguardando conexão de um cliente...')
    print(HOST)
    print(PORT)
    sc, endereco = recebe.accept()  # Aceita a conexão e obtém o objeto de soquete e o endereço do cliente
    print("Aceitei o cliente")
    while True:
        ler_fifo = sc.recv(1024)
        #dado = ler_fifo.decode("utf-8")
        hex_string = ' '.join(format(byte, '02x') for byte in ler_fifo) 
        fifo.put(hex_string)#else add no buffer
        print("Servidor foi chamado e escreveu na FIFO")
        print(fifo.qsize())

        '''while not fifo.empty():
            item = fifo.get()
            print("Item na FIFO:", item)'''

################### TIMER
def timer():#chama o decodificador a cada 0.1 ou 0.05 segundos
    print(Fore.GREEN + "Timer chamado!")
    while True:
        if fifo.qsize() >= MAX_SIZE_BUFFER:#CHEIO
            time.sleep(2)#Acelerando leitura de buffer
            print("Timer chamado: FIFO cheia")
            split(fifo.get())
        if fifo.empty():#se fifo estiver vazia
            print(Fore.RED + "Fifo vazia...")
        else:
            time.sleep(2)
            #print("Timer chamado: FIFO não cheia")
            split(fifo.get())
            
        #time.sleep(t)  # Espera "t" milissegundos

################### SPLIT
def split(vet):
    #encotrar size
    sizeA = int(vet[1], 16)
    print(f"Valor size: {sizeA}")#acho o size
    end = 1 + sizeA + 1
    print(f"Valor de END: {end}")
    ace = vet[:end]
    gyEmag = vet[end:]

    print(f"Valor de ACE: {ace}")    
    #print(f"Valor de GY E MAG : {gyEmag}")

    sizeG = int(gyEmag[1], 16)
    endG = 1 + sizeG + 1
    gy = gyEmag[endG:]
    mag = gyEmag[:endG]

    print(f"Valor de GY: {gy}")
    print(f"Valor de MAG: {mag}")
    decoder(ace)
    decoder(gy)
    decoder(mag)


################### DECODER
def decoder(data):
    while True:
        cmd = int(data[0],16)
        print(f"Valor cmd: {cmd}")
        size = int(data[1],16)
        print(f"Valor size: {size}")

        j = size
        for j in data: #Popula os dados no vetor de DADOS
            dadinho = int(j, 16)
            data.append(dadinho)

        crc1 = data[len(data)-1]
        data = data[2:]
        data.pop(-1)

        print(f"Comando = {cmd}, Size: {size}, Dados: {data}, CRC: {crc1}")   
        ################# TERMINO DA LEITURA
        crcV = 0

        print(f"Resultado de crcV: {crcV}")
        print(f"Resultado de cmd: {cmd}")
        print(f"Resultado de size: {size}")

        crcV = crcV ^ cmd
        print(f"Resultado: {crcV} ^ {cmd} -> {crcV}")
        crcV = crcV ^ size
        print(f"Resultado: {crcV} ^ {size} -> {crcV}")

        print(f"/////////////////////////////////////////////////////////")
        i = 0
        count = 0
        for i in data:
            print(f"Valor de I : {i}")
            crcV = crcV ^ i
            print(f"Posição: {count}. Resultado: {crcV} ^ {i} -> {crcV}")
            count += 1
        print(f"/////////////////////////////////////////////////////////")
        print(f"Resultado de crcV: {crcV}")
        print(f"Resultado de crc1: {crc1}")
        if(crcV == crc1):
            print(f"Dados consistentes.")
            print(f"Dados consistentes.")
        else:
            print(f"Erro de verificação.")
        
        crcV = 0
        data.clear()#limpa o vetor de dados para a proxima iteração de linha 


################### Crie as thread para as funções
thread1 = threading.Thread(target=servidor)
thread2 = threading.Thread(target=timer)
################### Inicia as threads
thread1.start()# Inicie o paralelismo para o servidor
time.sleep(0.5) 
thread2.start()# Inicie o paralelismo para o decodificador
time.sleep(0.5)