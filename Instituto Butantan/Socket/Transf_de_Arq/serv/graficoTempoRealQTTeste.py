import matplotlib.pyplot as plt
import csv
import datetime as dt
import socket
import time, sys
import tkinter as tk
import numpy as np
from tkinter import font
from collections import deque
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.style as mplstyle
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
#######  CLASSE CRONOMETRO
####################################

class Timer:
    def __init__(self):
        self.start = time.perf_counter()
    def reiniciar(self):
        self.start = time.perf_counter()
    def obter_tempo(self):
        return time.perf_counter() - self.start
####################################
#######  JANELAMENTO
####################################
text_port = Label(janela, 
                  text="Port:", 
                  font="Arial 10")#texto "Port:"
text_port.pack(side=tk.RIGHT,anchor=tk.N)

input_port = Entry(janela)#Caixa de texto para digitar o port
input_port.pack(side=tk.RIGHT,anchor=tk.N)

botao_serv = Button(janela, 
                    text="Listen", 
                    font="Arial 10 bold", 
                    fg='green',
                    command=lambda: serv(input_port))#sem o parentese, botao que roda a função
botao_serv.pack(side=tk.RIGHT,anchor=tk.N)


fonte_G = font.Font(family="Arial", size=20)
fonte_M = font.Font(family="Arial", size=15)
fonte_P = font.Font(family="Arial", size=8)

'''output_text = tk.Text(janela, wrap=tk.WORD, width=30, height=1.2,font=fonte_G)
output_text.pack(side=tk.RIGHT, anchor=tk.N)
'''
#text_port = Label(janela, text="Log:", font="Arial 20")
#text_port.pack(side=tk.LEFT,anchor=tk.N)
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
        sc = recebe.accept()
        arquivof = open("/Users/Rodrigo Girardi/Desktop/Base/Socket/Transf_de_Arq/serv/dataset.csv",'wb') #abrir o arquivo para escrita
        fim =0
        while (fim==0):       
            ler_bfferl = sc.recv(1024) #aloca no buffer o que foi recebido
            while (ler_bfferl):
                    arquivof.write(ler_bfferl)# escreve no arquivo o buffer recebido
                    ler_bfferl = sc.recv(1024) # aloca o resto no buffer
                    fim=1  

####################################
#######  Gráficos   
####################################
real_time = [] 

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

num_displayed = 100

real_time = deque(maxlen=num_displayed)

yAceleX = deque(maxlen=num_displayed)
yAceleY = deque(maxlen=num_displayed)
yAceleZ = deque(maxlen=num_displayed)

yGyroX = deque(maxlen=num_displayed)
yGyroY = deque(maxlen=num_displayed)
yGyroZ = deque(maxlen=num_displayed)

yAzimuth = deque(maxlen=num_displayed)
yPitch = deque(maxlen=num_displayed)
yRoll = deque(maxlen=num_displayed)

yLabel = deque(maxlen=num_displayed)

def Anime1(i):
    count = 0
    with open('BSC_1_1_annotated.csv','r') as arquivo_csv:
        Data=csv.DictReader(arquivo_csv)
        for a in Data:
            if(count == i):
                real_time.append(float(a['rel_time']))  

                yAceleX.append(float(a['acc_x']))
                yAceleY.append(float(a['acc_y'])) 
                yAceleZ.append(float(a['acc_z'])) 

                yGyroX.append(float(a['gyro_x'])) 
                yGyroY.append(float(a['gyro_y'])) 
                yGyroZ.append(float(a['gyro_z'])) 

                yAzimuth.append(float(a['azimuth'])) 
                yPitch.append(float(a['pitch'])) 
                yRoll.append(float(a['roll'])) 
                yLabel.append(str(a['label'])) 
            
            count = count+1
 
    maxGraphU = 20
    maxGraphL = -20

    plt.subplot(231).clear()
    plt.subplot(231)
    plt.title('Gráfico 1: Acelerometria XYZ')
    plt.plot(real_time, yAceleX,label='AceleX')
    plt.plot(real_time, yAceleY,label='AceleY')
    plt.plot(real_time, yAceleZ,label='AceleZ')
    plt.legend()
    plt.xlim(min(real_time), max(real_time))
    plt.ylim(maxGraphL, maxGraphU)

    plt.subplot(232).clear()
    plt.subplot(232)
    plt.title('Gráfico 2: Giroscopio XYZ')
    plt.plot(real_time, yGyroX,label='GyroX')
    plt.plot(real_time, yGyroY,label='GyroY')
    plt.plot(real_time, yGyroZ,label='GyroZ')
    plt.legend()
    plt.xlim(min(real_time), max(real_time))
    plt.ylim(maxGraphL, maxGraphU)

    plt.subplot(233).clear()
    plt.subplot(233)
    plt.title('Gráfico 3: Azimuth')
    plt.plot(real_time, yAzimuth,label='Azimuth')
    plt.ylim(100,300 )
    plt.legend()

    plt.subplot(234).clear()
    plt.subplot(234)
    plt.title('Gráfico 4: Pitch')
    plt.plot(real_time, yPitch,label='Pitch')
    plt.ylim(-100,100 )
    plt.legend()

    plt.subplot(235).clear()
    plt.subplot(235)
    plt.title('Gráfico 5: Roll')
    plt.plot(real_time, yRoll,label='Roll')
    plt.ylim(-70,70 )
    plt.legend()

    plt.subplot(236).clear()
    plt.subplot(236)
    plt.title('ATIVIDADE')
    plt.plot(real_time, yLabel,label='Label',color='red',linestyle='dashed', linewidth=2, markersize=12)
    plt.legend()


''' 
    #Atualize a saída na caixa de texto
    text_label = yLabel  # Substitua yLabel pelo texto que você deseja exibir
    #output_text.config(state=tk.NORMAL)  # Permita a edição do texto
    output_text.delete(1.0, tk.END)  # Limpe o texto anterior
    output_text.insert(tk.END, text_label)  # Insira o novo texto
    output_text.config(state=tk.DISABLED)  # Desabilite a edição do texto (apenas leitura)
'''


frame1 = tk.Frame(janela)
frame1.pack(side=tk.LEFT, anchor=tk.S)

fig1= plt.figure(figsize=(50, 10))
canvas1 = FigureCanvasTkAgg(fig1, master=frame1)
canvas1_widget = canvas1.get_tk_widget()
canvas1_widget.pack()


'''mplstyle.use('fast')
Ani1 = FuncAnimation(fig1, Anime1, interval=1)  # interval = tempo de plotagem (100=0.1s)'''


janela.mainloop()#ultima linha sempre
