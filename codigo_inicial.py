import requests
import matplotlib as mpl
import matplotlib.pyplot as plt
import csv
import datetime
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.collections import EventCollection


import numpy as np
from tkinter import *


def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    #cotacao_dolar_low = requisicao_dic['USDBRL']['low']
    #cotacao_euro_low = requisicao_dic['EURBRL']['low']
    #cotacao_btc_low = requisicao_dic['BTCBRL']['low']

    texto = f'''
    Dolar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''

    texto_cotação["text"] = texto

    data_atual = datetime.date.today()

    texto_escrita = f'{cotacao_dolar},{cotacao_euro},{cotacao_btc},{data_atual}'#dolar, euro, BTC, Data----CSV ;)
    escrever_em_arquivo(texto_escrita)


janela = Tk()
janela.title("Cotação atual da moedas")#titulo da janela
janela.geometry("700x700")

texto_orientacao = Label(janela, text="Exibir cotação das moedas", font="Arial 20")#texto
texto_orientacao.grid(column=0, row=0, padx=10,pady=10)#posição do texto linha=0 coluna =0

botao = Button(janela, text="Buscar cotações Dolar/Euro/BTC", font="Arial 20", command=pegar_cotacoes)#sem o parentese, botao que roda a função
botao.grid(column=0, row= 1, padx=10,pady=10)#posição do botao

texto_cotação = Label(janela, text="", font="Arial 20")
texto_cotação.grid(column=0,row=2,padx=10,pady=10)

######################################################################
##########      ESCRITA NO ARQUIVO: INICIO
######################################################################

def escrever_em_arquivo(texto_escrita):
    nome_arquivo = "data_set_coins.csv"
    with open(nome_arquivo, 'a') as arquivo:
        arquivo.write(texto_escrita + "\n")

######################################################################
##########      ESCRITA NO ARQUIVO: FIM
######################################################################

######################################################################
##########      GRAFICO: INICIO
######################################################################

#criando grafico
xdata1 = []
xdata2 = []
xdata3 = []
ydata = []
with open("data_set_coins.csv", "r") as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    for linha in leitor_csv:
        xdata1.append(float(linha['Dolar']))
        xdata2.append(float(linha['Euro']))
        xdata3.append(float(linha['BTC']))
        ydata.append(str(linha['Data']))



figura=plt.Figure(figsize=(10,6),dpi=60)
grafico=figura.add_subplot(111)

canvas=FigureCanvasTkAgg(figura,janela )
canvas.get_tk_widget().grid(column=0,row=3, padx=10,pady=10)




#x = np.linspace(0, 2, 100)  # Sample data.

# Note that even in the OO-style, we use `.pyplot.figure` to create the Figure.
grafico.plot(xdata1, ydata, label='Dolar')  # Plot some data on the axes.
grafico.plot(xdata2, ydata, label='Euro')  # Plot more data on the axes...
#grafico.plot(xdata3, ydata, label='BTC')  # ... and some more.
grafico.set_xlabel('Valor')  # Add an x-label to the axes.
grafico.set_ylabel('Data')  # Add a y-label to the axes.
grafico.set_title("Cotação")  # Add a title to the axes.
grafico.legend()  # Add a legend.


# Fixing random state for reproducibility

# create random data

# split the data into two parts

# sort the data so it makes clean curves
# create some y data points

######################################################################
##########      GRAFICO: FIM
######################################################################

janela.mainloop()#ultima linha sempre