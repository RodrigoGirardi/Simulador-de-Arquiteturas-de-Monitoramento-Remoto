import matplotlib.pyplot as plt
import csv
import tkinter as tk
from tkinter import font
from collections import deque
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.animation import FuncAnimation
import pandas as pd

# Criação da janela principal
janela = tk.Tk()
janela.title("LifeSenior Server - v0.1")
janela.geometry("1920x1080")
janela.configure(background='#dde')

fonte_G = font.Font(family="Arial", size=20)
fonte_M = font.Font(family="Arial", size=15)
fonte_P = font.Font(family="Arial", size=8)

# Inicialização dos dados
num_displayed = 500
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

# Função de animação
def animate(i, ax1, ax2, ax3, ax4, ax5, ax6, num_points):
    count = 0
    with open('data.csv', 'r') as arquivo_csv:
        Data = csv.DictReader(arquivo_csv)
        for a in Data:
            if count < i * num_points:
                count += 1
                continue

            if count >= (i + 1) * num_points:
                break
            real_time.append(float(a['timestamp']))
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
            count += 1

    maxGraphU = 20
    maxGraphL = -20

    ax1.clear()
    ax1.plot(real_time, yAceleX, label='AceleX')
    ax1.plot(real_time, yAceleY, label='AceleY')
    ax1.plot(real_time, yAceleZ, label='AceleZ')
    ax1.legend()
    ax1.set_title('Gráfico 1: Acelerometria XYZ')
    ax1.set_xlim(min(real_time), max(real_time))
    ax1.set_ylim(maxGraphL, maxGraphU)

    ax2.clear()
    ax2.plot(real_time, yGyroX, label='GyroX')
    ax2.plot(real_time, yGyroY, label='GyroY')
    ax2.plot(real_time, yGyroZ, label='GyroZ')
    ax2.legend()
    ax2.set_title('Gráfico 2: Giroscopio XYZ')
    ax2.set_xlim(min(real_time), max(real_time))
    ax2.set_ylim(maxGraphL, maxGraphU)

    ax3.clear()
    ax3.plot(real_time, yAzimuth, label='Azimuth')
    ax3.legend()
    ax3.set_title('Gráfico 3: Azimuth')
    ax3.set_ylim(0, 500)

    ax4.clear()
    ax4.plot(real_time, yPitch, label='Pitch')
    ax4.legend()
    ax4.set_title('Gráfico 4: Pitch')
    ax4.set_ylim(-100, 100)

    ax5.clear()
    ax5.plot(real_time, yRoll, label='Roll')
    ax5.legend()
    ax5.set_title('Gráfico 5: Roll')
    ax5.set_ylim(-70, 70)

    ax6.clear()
    ax6.plot(real_time, yLabel, label='Label', color='red', linestyle='dashed', linewidth=2, markersize=12)
    ax6.legend()
    ax6.set_title('ATIVIDADE')


# Inicialização dos subplots
#fig1, axs = plt.subplots(2, 3, figsize=(50, 10))
fig1, axs = plt.subplots(3, 2, figsize=(50, 10))

# Frame do Matplotlib
frame1 = tk.Frame(janela)
frame1.pack(side=tk.LEFT, anchor=tk.S)

# Configuração do canvas do Matplotlib
canvas1 = FigureCanvasTkAgg(fig1, master=frame1)
canvas1_widget = canvas1.get_tk_widget()
canvas1_widget.pack()

num_points = 25

# Inicialização da animação
#ani = FuncAnimation(fig1, animate, fargs=(axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1], axs[2, 1], axs[2, 2], num_points), interval=500)#0.5 segundos  === interval = 500
ani = FuncAnimation(fig1, animate, fargs=(axs[0, 0], axs[0, 1], axs[1, 0], axs[1, 1], axs[2, 0], axs[2, 1], num_points), interval=500)

# Execução da aplicação
janela.mainloop()