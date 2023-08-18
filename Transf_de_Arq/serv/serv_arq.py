import socket
import csv
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.collections import EventCollection
from datetime import datetime
from tkinter import *

janela = Tk()
janela.title("LifeSenior Server")#titulo da janela
janela.geometry("1920x1080")
janela.configure(background='#dde')



######################################
##    CSV
######################################
def toCsv():
    with open('dataset.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        cont = 0
        # Itera pelas linhas do arquivo CSV
        for linha in leitor_csv:
            
            timestamp = int(linha['timestamp'])
            timeConv = datetime.fromtimestamp(timestamp)
            miliseconds = int(linha['miliseconds'])  

            accelerationX = int(linha['acceleration - x axis'])
            accelerationY = int(linha['acceleration - y axis'])
            accelerationZ = int(linha['acceleration - z axis'])

            gyroscopeX = int(linha['gyroscope - x axis'])
            gyroscopeY = int(linha['gyroscope - y axis'])
            gyroscopeZ = int(linha['gyroscope - z axis'])

            magnetometreX = int(linha['magnetometer - x axis'])
            magnetometreY = int(linha['magnetometer - y axis'])
            magnetometreZ = int(linha['magnetometer - z axis'])

            eda = int(linha['EDA'])
            ibi = int(linha['IBI'])
            temperature = int(linha['temperature'])


            print(f"##############################")
            print(f"###     Dado: {cont} ")
            print(f"##############################")
            print(f"Timestamp: {timeConv}, Miliseconds: {miliseconds}")
            print(f"Aceleration X: {accelerationX}, Aceleration Y: {accelerationY}, Aceleration Z: {accelerationZ}")
            print(f"Gyroscope X: {gyroscopeX}, Gyroscope Y: {gyroscopeY}, Gyroscope Z: {gyroscopeZ}")
            print(f"Magnetometre X: {magnetometreX}, Magnetometre Y: {magnetometreY}, Magnetometre Z: {magnetometreZ}")
            print(f"EDA: {eda}, IBI: {ibi} , Temperature: {temperature}C°")
            cont += 1



######################################
##    Servidor
######################################
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
def plotGraf():
    timeConv = []

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
    #yIbi = []
    #yTemperature = []

    with open('BSC_1_1_annotated.csv', 'r', newline='') as arquivo_csv:
        leitor_csv = csv.DictReader(arquivo_csv)
        cont = 0
        # Itera pelas linhas do arquivo CSV
        for linha in leitor_csv:
            
            timestamp = int(linha['timestamp'])
            timestamp = timestamp/1000
            timeConv.append(datetime.fromtimestamp(timestamp))
            rel_time = float(linha['rel_time'])  

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
            #yIbi.append(int(linha['IBI']))
            #yTemperature.append(int(linha['temperature']))

            '''
            print(f"##############################")
            print(f"###     Dado: {cont} ")
            print(f"##############################")
            print(f"Timestamp: {timeConv}, Miliseconds: {rel_time}")
            print(f"Aceleration X: {yAceleX}, Aceleration Y: {yAceleY}, Aceleration Z: {yAceleZ}")
            print(f"Gyroscope X: {yGyroX}, Gyroscope Y: {yGyroY}, Gyroscope Z: {yGyroZ}")
            print(f"Azimuth: {yAzimuth}, Pitch: {yPitch}, Roll: {yRoll}")
            print(f"Label: {yLabel}")
            '''
            #cont += 1


    
    grafAceleX=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafAceleX.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafAceleX,janela )
    canvas.get_tk_widget().grid(column=0,row=4, padx=2,pady=2)
    grafico.plot(timeConv, yAceleX,marker = 'o', label='Acele X')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Acele X')  # Add a y-label to the axes.
    grafico.set_title("Acelerometria X")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafAceleY=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafAceleY.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafAceleY,janela )
    canvas.get_tk_widget().grid(column=0,row=5, padx=2,pady=2)
    grafico.plot(timeConv, yAceleY,marker = 'o', label='Acele Y')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Acele Y')  # Add a y-label to the axes.
    grafico.set_title("Acelerometria Y")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafAceleZ=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafAceleZ.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafAceleZ,janela )
    canvas.get_tk_widget().grid(column=0,row=6, padx=2,pady=2)
    grafico.plot(timeConv, yAceleZ,marker = 'o', label='Acele Z')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Acele Z')  # Add a y-label to the axes.
    grafico.set_title("Acelerometria Z")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafGiroX=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafGiroX.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafGiroX,janela )
    canvas.get_tk_widget().grid(column=0,row=7, padx=2,pady=2)
    grafico.plot(timeConv, yGyroX,marker = 'o', label='Giro X')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Giro X')  # Add a y-label to the axes.
    grafico.set_title("Giroscopio X")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafGiroY=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafGiroY.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafGiroY,janela )
    canvas.get_tk_widget().grid(column=0,row=8, padx=2,pady=2)
    grafico.plot(timeConv, yGyroY,marker = 'o', label='Giro Y')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Giro Y')  # Add a y-label to the axes.
    grafico.set_title("Giroscopio Y")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafGiroZ=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafGiroZ.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafGiroZ,janela )
    canvas.get_tk_widget().grid(column=0,row=9, padx=2,pady=2)
    grafico.plot(timeConv, yGyroZ,marker = 'o', label='Giro Z')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Giro Z')  # Add a y-label to the axes.
    grafico.set_title("Giroscopio Z")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafAzi=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafAzi.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafAzi,janela )
    canvas.get_tk_widget().grid(column=1,row=4, padx=2,pady=2)
    grafico.plot(timeConv, yAzimuth,marker = 'o', label='Azimuth')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Azimuth')  # Add a y-label to the axes.
    grafico.set_title("Azimuth")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafPitch=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafPitch.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafPitch,janela )
    canvas.get_tk_widget().grid(column=1,row=5, padx=2,pady=2)
    grafico.plot(timeConv, yPitch,marker = 'o', label='Pitch')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Pitch')  # Add a y-label to the axes.
    grafico.set_title("Pitch")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafRoll=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafRoll.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafRoll,janela )
    canvas.get_tk_widget().grid(column=1,row=6, padx=2,pady=2)
    grafico.plot(timeConv, yRoll,marker = 'o', label='Roll')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Roll')  # Add a y-label to the axes.
    grafico.set_title("Roll")  # Add a title to the axes.
    grafico.legend()  # Add a legend.
'''
    grafEda=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafEda.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafEda,janela )
    canvas.get_tk_widget().grid(column=1,row=7, padx=2,pady=2)
    grafico.plot(timeConv, yEda,marker = 'o', label='Eda')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('EDA')  # Add a y-label to the axes.
    grafico.set_title("EDA")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafIbi=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafIbi.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafIbi,janela )
    canvas.get_tk_widget().grid(column=1,row=8, padx=2,pady=2)
    grafico.plot(timeConv, yIbi,marker = 'o', label='Ibi')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('IBI')  # Add a y-label to the axes.
    grafico.set_title("IBI")  # Add a title to the axes.
    grafico.legend()  # Add a legend.

    grafTemp=plt.Figure(figsize=(15,2),dpi=60)
    grafico=grafTemp.add_subplot(111)
    canvas=FigureCanvasTkAgg(grafTemp,janela )
    canvas.get_tk_widget().grid(column=1,row=9, padx=2,pady=2)
    grafico.plot(timeConv, yTemperature,marker = 'o', label='Temperature')  # Plot some data on the axes.
    #grafico.set_xlabel('Date')  # Add an x-label to the axes.
    grafico.set_ylabel('Temp')  # Add a y-label to the axes.
    grafico.set_title("Temperature")  # Add a title to the axes.
    grafico.legend()  # Add a legend.
'''
    
plotGraf()

####################################
#######  Dimensões da Janela
####################################


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

text_port = Label(janela, 
                  text="Port:", 
                  font="Arial 10")#texto "Port:"
text_port.grid(column=0, row=0, padx=0,pady=1)


input_port = Entry(janela)#Caixa de texto
input_port.grid(column=1, row=0, padx=0,pady=1)


botao_serv = Button(janela, 
                    text="Listen", 
                    font="Arial 10 bold", 
                    fg='green',
                    command=lambda: serv(input_port))#sem o parentese, botao que roda a função
botao_serv.grid(column=3, row= 0, padx=10,pady=10)#posição do botao

#text_port = Label(janela, text="port: " + input_port, font="Arial 10")#texto "Port:"
#text_port.grid(column=0, row=1, padx=0,pady=1)

text_box = Text(janela, width=40,height=10)
text_box.grid(column=0, row=2, padx=10,pady=10)



janela.mainloop()#ultima linha sempre