import socket
import csv
import time
import matplotlib.pyplot as plt
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
from tkinter import *

####################################
#######  INICIALIZAÇÃO DA JANELA
####################################

janela = Tk()
janela.title("LifeSenior Server")#titulo da janela
janela.geometry("1920x1080")
janela.configure(background='#dde')

####################################
#######  SERVIDOR
####################################
def serv(input_port):
    HOST = 'localhost'
    PORT = int(input_port.get())

    recebe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#socket.socket()
    recebe.bind((HOST,PORT))#ip que vai ouvir e a porta
    recebe.listen(10) # numero de conexões não aceitas, antes de recusar novas
    print('Aguardando conexão de um cliente...')
    print(HOST)
    print(PORT)

    while True:
        sc, ender = recebe.accept()

        arquivof = open("/Users/Rodrigo Girardi/Desktop/Base/Socket/Transf_de_Arq/serv/dataset.csv",'wb') #abrir o arquivo para escrita
        fim =0
        while (fim==0):       
        
            ler_bfferl = sc.recv(1024) #aloca no buffer o que foi recebido
            
            while (ler_bfferl):
                    
                    arquivof.write(ler_bfferl)# escreve no arquivo o buffer recebido
                    ler_bfferl = sc.recv(1024) # aloca o resto no buffer
                    
                    fim=1
                    
        arquivof.close()

        sc.close()

####################################
#######  Gráficos   
####################################
#Importante: https://www.youtube.com/watch?v=BeLAWsh9zJE    
def plotGraf():
    timeConv = []
    rel_time = []
    yAceleX = []
    yAceleY = []
    yAceleZ = []

    yGyroX = []
    yGyroY = []
    yGyroZ = []

    yAzimuth = []
    yPitch = []
    yRoll = []

    yLabel = []

    with open('BSC_1_1_annotated.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        # Itera pelas linhas do arquivo CSV
        for linha in leitor_csv:
            
            timeConv.append(int(linha['timestamp']))
            rel_time.append(float(linha['rel_time']))  

            yAceleX.append(float(linha['acc_x']))
            yAceleY.append(float(linha['acc_y']))
            yAceleZ.append(float(linha['acc_z']))

            yGyroX.append(float(linha['gyro_x']))
            yGyroY.append(float(linha['gyro_y']))
            yGyroZ.append(float(linha['gyro_z']))

            yAzimuth.append(float(linha['azimuth']))
            yPitch.append(float(linha['pitch']))
            yRoll.append(float(linha['roll']))

            yLabel.append(linha['label'])


        

    grafAceleX=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafAceleX.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafAceleX,janela )
    canvas.get_tk_widget().grid(column=0,row=4, padx=2,pady=2)
    grafico.plot(timeConv, yAceleX,marker = '.', label='Acele X')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Acele X')  # Add a y-label to the axes.
    grafico.set_title("Acelerometria X")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafAceleY=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafAceleY.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafAceleY,janela )
    canvas.get_tk_widget().grid(column=0,row=5, padx=2,pady=2)
    grafico.plot(timeConv, yAceleY,marker = '.', label='Acele Y')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Acele Y')  # Add a y-label to the axes.
    grafico.set_title("Acelerometria Y")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafAceleZ=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafAceleZ.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafAceleZ,janela )
    canvas.get_tk_widget().grid(column=0,row=6, padx=2,pady=2)
    grafico.plot(timeConv, yAceleZ,marker = '.', label='Acele Z')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Acele Z')  # Add a y-label to the axes.
    grafico.set_title("Acelerometria Z")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafGiroX=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafGiroX.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafGiroX,janela )
    canvas.get_tk_widget().grid(column=0,row=7, padx=2,pady=2)
    grafico.plot(timeConv, yGyroX,marker = '.', label='Giro X')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Giro X')  # Add a y-label to the axes.
    grafico.set_title("Giroscopio X")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafGiroY=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafGiroY.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafGiroY,janela )
    canvas.get_tk_widget().grid(column=0,row=8, padx=2,pady=2)
    grafico.plot(timeConv, yGyroY,marker = '.', label='Giro Y')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Giro Y')  # Add a y-label to the axes.
    grafico.set_title("Giroscopio Y")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafGiroZ=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafGiroZ.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafGiroZ,janela )
    canvas.get_tk_widget().grid(column=0,row=9, padx=2,pady=2)
    grafico.plot(timeConv, yGyroZ,marker = '.', label='Giro Z')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Giro Z')  # Add a y-label to the axes.
    grafico.set_title("Giroscopio Z")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafAzi=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafAzi.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafAzi,janela )
    canvas.get_tk_widget().grid(column=1,row=4, padx=2,pady=2)
    grafico.plot(timeConv, yAzimuth,marker = '.', label='Azimuth')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Azimuth')  # Add a y-label to the axes.
    grafico.set_title("Azimuth")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafPitch=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafPitch.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafPitch,janela )
    canvas.get_tk_widget().grid(column=1,row=5, padx=2,pady=2)
    grafico.plot(timeConv, yPitch,marker = '.', label='Pitch')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Pitch')  # Add a y-label to the axes.
    grafico.set_title("Pitch")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafRoll=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafRoll.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafRoll,janela )
    canvas.get_tk_widget().grid(column=1,row=6, padx=2,pady=2)
    grafico.plot(timeConv, yRoll,marker = '.', label='Roll')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Roll')  # Add a y-label to the axes.
    grafico.set_title("Roll")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

'''
    mensagem = (timeConv)
    text_box = Text(janela, width=100,height=7)
    text_box.grid(column=1, row=8, padx=10,pady=10)
    text_box.insert(tk.END, mensagem + "\n")
    text_box.see(tk.END) 
'''

plotGraf()

####################################
#######  JANELAMENTO
####################################
text_port = Label(janela, 
                  text="Port:", 
                  font="Arial 10")#texto "Port:"
text_port.grid(column=0, row=0, padx=0,pady=1)

input_port = Entry(janela)#Caixa de texto para digitar o port
input_port.grid(column=1, row=0, padx=0,pady=1)


botao_serv = Button(janela, 
                    text="Listen", 
                    font="Arial 10 bold", 
                    fg='green',
                    command=lambda: serv(input_port))#sem o parentese, botao que roda a função
botao_serv.grid(column=3, row= 0, padx=10,pady=10)#posição do botao

text_port = Label(janela, text="Log:", font="Arial 20")
text_port.grid(column=1, row=7, padx=0,pady=1)

####################################
#######  LOG
####################################


janela.mainloop()#ultima linha sempre