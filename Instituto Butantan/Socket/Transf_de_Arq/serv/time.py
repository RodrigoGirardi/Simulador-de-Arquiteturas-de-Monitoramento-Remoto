import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import csv
from scipy.optimize import curve_fit
import numpy as np
''' 
fig=plt.figure()
gráfico=fig.add_subplot(111)

start=time.time()

xs=[]
ys=[]

def reta(x,a,b):
    return a*x+b

def atualiza(i):
    dados=open("C:/Users/Rodrigo Girardi/Desktop/Base/Instituto Butantan/Socket/Transf_de_Arq/teste.txt.","r").read()
    linhas=dados.split("\n")
    for y in linhas:
        if len(y)>0:
            ys.append(float(y))
            if len(xs)==0:
                xs.append(time.time()-start)
            if len(ys)>len(xs):
                x=time.time()-start
                xs.append(x)
    gráfico.clear()
    if len(xs)>1:
        parametros, erro = curve_fit(reta, xs, ys)
        xFit=np.arange(0,xs[-1]+0.1, 0.1)
        gráfico.plot(xFit, reta(xFit, *parametros))
        plt.title("Valor digitado em função do tempo\na = {0}\nb = {1}".format(parametros[0], parametros[1]))
    else:
        plt.title("Valor digitado em função do tempo")
    gráfico.plot(xs,ys,"-o")
    plt.xlabel("Tempo (s)")
    plt.ylabel("Valor digitado")
    #plt.title("Valor digitado em função do tempo")
    ys.clear()
    
a=animation.FuncAnimation(fig, atualiza, interval=1)
plt.show()
'''

def draw_flow(self, test_data, test_label):
    data_size = test_data.shape[0]

    x = [_ for _ in range(150)]
    ax = [0 for _ in range(150)]
    ay = [0 for _ in range(150)]
    az = [0 for _ in range(150)]

    run_step = 10
    num = int(data_size / run_step)

    start_time = time.time()

    plt.axis([0, 151, -20, 20])
    plt.ion()
    for i in range(num):
        if i > int(time_step/run_step):
            predict = run.run(test_data[i * run_step - time_step: i * run_step, :])
            title = 'correct:' + Label[test_label[i * run_step]] + '     predict:' + Label[predict[int(time_step - 1)][0]]
        else:
            title = 'correct:' + Label[test_label[i * run_step]] + '     predict:' + 'unknow'

        self._update_show_data(ax, run_step, test_data[i * run_step:i * run_step + run_step, 0])
        self._update_show_data(ay, run_step, test_data[i * run_step:i * run_step + run_step, 1])
        self._update_show_data(az, run_step, test_data[i * run_step:i * run_step + run_step, 2])

        plt.cla()
        plt.plot(x, ax)
        plt.plot(x, ay)
        plt.plot(x, az)

        plt.title(title)
        plt.draw()
        plt.pause(0.001)

    during = str(time.time() - start_time)
    print('检测耗时=', during)