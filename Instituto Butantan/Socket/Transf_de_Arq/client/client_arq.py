import socket


HOST = 'localhost'
PORT = 55555

envia = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket.socket()
envia.connect((HOST,PORT))# IP e a porta usada no servidor
envia.sendall(str.encode('Funcionou aqui! :) '))
arquivo = open("/Users/Rodrigo Girardi/Desktop/Base/Socket/Transf_de_Arq/client/oi.txt", "rb")# nome do arqquivo
ler_buffer = arquivo.read(1024) #começa a ler o arquivo e armazenar em um buffer
##C:\Users\Rodrigo Girardi\Desktop\Base\Socket\Transf_de_Arq\client\oi.txt

##arquivo = open("/Users/Rodrigo Girardi/Desktop/Base/Socket/Transf_de_Arq/client/oi.txt", "rb")
while (ler_buffer):
    envia.send(ler_buffer) #envia o condeudo do buffer para o servidor
    ler_buffer = arquivo.read(1024)# armazena mais conteudo do arquivo no buffer
envia.close()
