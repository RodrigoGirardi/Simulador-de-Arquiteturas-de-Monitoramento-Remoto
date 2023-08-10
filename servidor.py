import socket
import functools
from tkinter import *

def listen(input_port):
    HOST = '10.32.162.153'
    PORT = int(input_port)  # Convertendo a entrada para inteiro

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, PORT))
    s.listen()
    print('Aguardando conexão de um cliente')
    print(PORT)
    conn, ender = s.accept()

    print('Conectado em ', ender)

    while True:
        data = conn.recv(1024)
        if not data:
            print('Fechando a conexão')
            conn.close()
            break
        conn.sendall(data)

#def get_port(input_port):
 #   entered_text = input_port.get()
  #  print("Port lido: " + entered_text)
   # listen()
####################################
#######  Dimensões da Janela
####################################
janela = Tk()
janela.title("LifeSenior Server")
janela.geometry("500x500")
janela.configure(background='#dde')

text_port = Label(janela, text="Port:", font="Arial 10")
text_port.grid(column=0, row=0, padx=0, pady=1)

input_port = Entry(janela)
input_port.grid(column=1, row=0, padx=0, pady=1)

botao_port = Button(janela, text="Change Port", font="Arial 10 bold", fg='green', command=functools.partial(listen, input_port.get()))
botao_port.grid(column=2, row=0, padx=10, pady=10)

#botao_listen = Button(janela, text="Listen", font="Arial 10 bold", fg='green', command=lambda: listen(entered_text))
#botao_listen.grid(column=3, row=0, padx=10, pady=10)

janela.mainloop()