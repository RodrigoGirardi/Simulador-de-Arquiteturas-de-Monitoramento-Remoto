import matplotlib.pyplot as plt
import csv
from matplotlib.animation import FuncAnimation as Funk
import datetime as dt
import socket
import time, sys
from collections import deque
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
from tkinter import *

####################################
#######  INICIALIZAÇÃO DA JANELA
####################################
'''
janela = Tk()
janela.title("LifeSenior Server")#titulo da janela
janela.geometry("1920x1080")
janela.configure(background='#dde')
'''
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


x=[]
y=[]

timeConv = []
real_time = []
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
cronometro = Timer()
# Função para rolar o gráfico

# Número de pontos a serem exibidos na tela (últimos 30 segundos)
num_displayed = 200

# Inicialize as listas e o deque para armazenar os dados
x = deque(maxlen=num_displayed)
yAceleX = deque(maxlen=num_displayed)

def Anime1(i):
    
    count = 0
    with open('BSC_1_1_annotated.csv','r') as arquivo_csv:
        Data=csv.DictReader(arquivo_csv)
        for a in Data:
            if(count == i):
                
                #x.append(float(a[1]))
                #x.append(dt.datetime.now().strftime('%H:%M:%S.%f'))
                #y.append(float(a[0])) 

                #timeConv.append(int(a['timestamp']))

                x.append(float(a['rel_time']))  

                yAceleX.append(float(a['acc_x']))
                '''
                yAceleY.append(float(a['acc_y']))
                yAceleZ.append(float(a['acc_z']))

                yGyroX.append(float(a['gyro_x']))
                yGyroY.append(float(a['gyro_y']))
                yGyroZ.append(float(a['gyro_z']))

                yAzimuth.append(float(a['azimuth']))
                yPitch.append(float(a['pitch']))
                yRoll.append(float(a['roll']))

                yLabel.append(a['label'])

                #print(y[-1],x[-1])
                '''
            count = count+1
    plt.clf()
    
    plt.subplot(111).clear()
    plt.subplot(111)
    plt.plot(x, yAceleX)

    plt.xlim(min(x), max(x))
    plt.ylim(min(yAceleX), max(yAceleX))
'''
        grafAceleX=plt.Figure(figsize=(15,2),dpi=60)  
        grafico=grafAceleX.add_subplot(111)
        canvas=FigureCanvasTkAgg(grafAceleX,janela )
        canvas.get_tk_widget().grid(column=0,row=4, padx=2,pady=2)
        grafico.plot(timeConv, yAceleX,marker = '.', label='Acele X')  # Plot some data on the axes.
'''
plt.figure(figsize=(10, 4))
Ani1= Funk(plt.gcf(),Anime1,interval=1)#interval = tempo de plotagem 100=0.1s


plt.tight_layout()
plt.show()



'''
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
'''