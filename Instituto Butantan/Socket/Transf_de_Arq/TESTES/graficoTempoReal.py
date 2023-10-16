import matplotlib.pyplot as plt
import csv
import datetime as dt
import socket
import time, sys
import tkinter as tk
import pandas as pd

from collections import deque
from matplotlib.animation import FuncAnimation as Funk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.animation import FuncAnimation
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

num_displayed = 400
maxGraphU = 20
maxGraphL = -20

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

def Leitura():
    with open('BSC_1_1_annotated.csv','r') as csvfile:
        Data=csv.DictReader(csvfile)
        for linha in Data:
                    real_time.append(float(linha['rel_time']))  

                    yAceleX.append(float(linha['acc_x']))
                    yAceleY.append(float(linha['acc_y'])) 
                    yAceleZ.append(float(linha['acc_z'])) 

                    yGyroX.append(float(linha['gyro_x'])) 
                    yGyroY.append(float(linha['gyro_y'])) 
                    yGyroZ.append(float(linha['gyro_z'])) 

                    yAzimuth.append(float(linha['azimuth'])) 
                    yPitch.append(float(linha['pitch'])) 
                    yRoll.append(float(linha['roll'])) 
                    #yLabel.append(str(linha['label'])) 

Leitura()#preenche os vetores com os dados do arquivo

def plotAceXYZ():
    plt.clf()  # Limpa o gráfico para recriá-lo
    plt.subplot(111)  # Cria um único subplot
    plt.subplot(111).clear()
    plt.plot(real_time, yAceleX, label='AceleX')
    plt.plot(real_time, yAceleY, label='AceleY')
    plt.plot(real_time, yAceleZ, label='AceleZ')
    plt.xlim(min(real_time), max(real_time))
    plt.ylim(maxGraphL, maxGraphU)
    plt.show()

plotAceXYZ()




#janela.mainloop()