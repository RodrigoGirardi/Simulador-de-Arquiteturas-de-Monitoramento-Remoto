import socket
import threading
import time
import csv
from typing import Deque, Any
from collections import deque
import queue ###   https://www.guru99.com/python-queue-example.html
from colorama import Fore, Back, Style, init


MAX_SIZE_BUFFER = 2000
init(autoreset=True)
fifo = queue.Queue()

################### SERVIDOR
def servidor():
    HOST = '10.32.160.172'
    PORT = 5555
    recebe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    recebe.bind(('10.32.160.172', 5555))
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
            print("Timer chamado: FIFO cheia")
            dataFifo = fifo.get()
            hex_string = ' '.join(format(byte, '02x') for byte in dataFifo)
            hex_parts = hex_string.split()
            split(hex_parts)
            time.sleep(0.2)#Acelerando leitura de buffer
        if fifo.empty():#se fifo estiver vazia
            print(Fore.RED + "Fifo vazia...")
            time.sleep(0.2)#
        else:
            #print("Timer chamado: FIFO não cheia")
            dataFifo = fifo.get()
            hex_string = ' '.join(format(byte, '02x') for byte in dataFifo)
            hex_parts = hex_string.split()
            split(hex_parts)
            time.sleep(0.1)
        #time.sleep(t)  # Espera "t" milissegundos
################### Funcao de escrita no arquivo
arq = "packOk.csv"
def escrita(pack):
    with open(arq, mode='a', newline='') as arquivo_csv:
        escritor_csv = csv.writer(arquivo_csv)
        # Escreva os dados no arquivo CSV
        escritor_csv.writerow(pack)
################### SPLIT
crcV = 0
pacoteOk = []
def split(vet):
    while len(vet) > 0:
        crcV = 0
        cmd1 = vet[0]
        size1 = vet[1]
        cmd = int(vet[0], 16)
        size = int(vet[1], 16)
        posCrc = size + 1
        crc = int(vet[posCrc], 16)
        crc1 = vet[posCrc]
        print(f"Valor Comando: {cmd}")
        print(f"Valor size: {size}")
        print(f"Valor crc: {crc}")
        if cmd >= 0 and cmd <= 4: #cmd correto
            print(f"Valor Comando: {cmd}")
            pacoteOk.append(cmd1)
            
            if size >= 0 and size <= 99:
                print(f"Valor Size: {size}")
                pacoteOk.append(size1)
                
                crcV = crcV ^ cmd
                print(f"Resultado: {crcV} ^ {cmd} -> {crcV}")
                crcV = crcV ^ size
                print(f"Resultado: {crcV} ^ {size} -> {crcV}")
                i = 1
                pos = 2
                while (i < size):
                    crcP = crcV
                    crcV = crcV ^ int(vet[pos], 16)
                    pacoteOk.append(vet[pos])
                    print(f"Resultado verifi: {crcP} ^ {int(vet[pos], 16)} -> {crcV}")
                    i += 1
                    pos += 1
                if crcV == crc:
                    print(f"Valor CRC: {crc}")
                    pacoteOk.append(crc1)
                    for item in pacoteOk:
                        if item in vet:
                            vet.remove(item)
                    print(f"Pacote OK: {pacoteOk}")
                    print(f"Pacote da fifo: {vet}")
                    print(f"Dado consistente.")
                    escrita(pacoteOk)
                    pacoteOk.clear()#limpa para a proxima iteração

                else:
                    print(f"Pacote OK: {pacoteOk}")
                    print(f"Valor CRC: {crc}")
                    print(f"Pacote da fifo: {vet}")
                    print(f"Dado inconsistente.")
            else:#size inconsistente
                crcV = 0
                crcV = crcV ^ cmd
                #print(f"Resultado: {crcV} ^ {cmd} -> {crcV}")
                crcV = crcV ^ size
                #print(f"Resultado: {crcV} ^ {size} -> {crcV}")
                for size in vet:
                    crcV = crcV ^ vet[size]

        else:#cmd inconsistente
            size = int(vet[1], 16)
            for size in vet:
                vet.pop(size)
            vet.pop(cmd)


################### Crie as thread para as funções
thread1 = threading.Thread(target=servidor)
thread2 = threading.Thread(target=timer)
################### Inicia as threads
thread1.start()# Inicie o paralelismo para o servidor
time.sleep(0.5) 
thread2.start()# Inicie o paralelismo para o decodificador
time.sleep(0.5)