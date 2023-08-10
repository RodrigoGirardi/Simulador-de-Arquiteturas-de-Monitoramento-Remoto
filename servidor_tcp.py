import socket
from tkinter import *



def listen(input_port):
    HOST =  '127.0.0.1'
    PORT = int(input_port.get())

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print('Aguardando conexão de um cliente')
    print(PORT)
    conn, ender = s.accept()

    print ('Conectado em ', ender)

    while True:
        data = conn.recv(1024)
        if not data:
            print('Fechando a conexão')
            conn.close()
            break
        conn.sendall(data)

####################################
#######  Dimensões da Janela
####################################
janela = Tk()
janela.title("LifeSenior Server")#titulo da janela
janela.geometry("500x500")
janela.configure(background='#dde')

####################################
#######  Exemplo de texto
####################################

#texto_orientacao = Label(janela, text="Exibir cotação das moedas", font="Arial 20")#texto
#texto_orientacao.grid(column=0, row=0, padx=10,pady=10)#posição do texto linha=0 coluna =0


####################################
#######  Cores
####################################
'''
RGB
Verde: #008000
Blue: #0000FF
Red: #FF0000
Yellow: #FFFF00
'''

text_port = Label(janela, text="Port:", font="Arial 10")#texto "Port:"
text_port.grid(column=0, row=0, padx=0,pady=1)

input_port = Entry(janela)#Caixa de texto
input_port.grid(column=1, row=0, padx=0,pady=1)


botao_listen = Button(janela, text="Listen", 
                      font="Arial 10 bold", fg='green',
                      command=lambda: listen(input_port))#sem o parentese, botao que roda a função
botao_listen.grid(column=3, row= 0, padx=10,pady=10)#posição do botao

#text_port = Label(janela, text="port: " + input_port, font="Arial 10")#texto "Port:"
#text_port.grid(column=0, row=1, padx=0,pady=1)

text_box = Text(janela, width=40,height=10)
text_box.grid(column=0, row=2, padx=10,pady=10)



janela.mainloop()#ultima linha sempre