import socket

recebe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

recebe.bind(('10.32.160.83', 3535))

recebe.listen(1)

print('Aguardando conexão de um cliente...')
print('10.32.160.83')
print(3535)

sc, endereco = recebe.accept()  # Aceita a conexão e obtém o objeto de soquete e o endereço do cliente
ler_buffer = sc.recv(1024)

arquivof = open("/Users/Rodrigo Girardi/Desktop/Base/Instituto Butantan/Socket/Transf_de_Arq/dataset.csv", 'wb')

sc = recebe.accept()
arquivof = open("/Users/Rodrigo Girardi/Desktop/Base/Socket/Transf_de_Arq/serv/dataset.csv",'wb') #abrir o arquivo para escrita
ler_bfferl = sc.recv(1024) #aloca no buffer o que foi recebido
arquivof.write(ler_bfferl)# escreve no arquivo o buffer recebido
ler_bfferl = sc.recv(1024) # aloca o resto no buffer

arquivof.close()
sc.close()


