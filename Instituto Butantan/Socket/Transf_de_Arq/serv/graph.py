import time
import matplotlib.pyplot as plt
import random
import csv
import pandas as pd


timeConv = []
rel_time = []
#yAceleX = []
yAceleY = []
yAceleZ = []

yGyroX = []
yGyroY = []
yGyroZ = []

yAzimuth = []
yPitch = []
yRoll = []

yLabel = []


'''
with open('BSC_1_1_annotated.csv', 'r', newline='') as arquivo_csv:
    leitor_csv = csv.DictReader(arquivo_csv)
    # Itera pelas linhas do arquivo CSV
    for linha in leitor_csv:
        
        timestamp = (linha['timestamp'])
       
        rel_time.append(float(linha['rel_time']))  

        #yAceleX.append(float(linha['acc_x']))
        yAceleY.append(float(linha['acc_y']))
        yAceleZ.append(float(linha['acc_z']))

        yGyroX.append(float(linha['gyro_x']))
        yGyroY.append(float(linha['gyro_y']))
        yGyroZ.append(float(linha['gyro_z']))

        yAzimuth.append(float(linha['azimuth']))
        yPitch.append(float(linha['pitch']))
        yRoll.append(float(linha['roll']))

        yLabel.append(linha['label'])
'''

fig = plt.figure()
ax = fig.add_subplot()
fig.show()

x = []
y = []  # List to store Y values

#n = 150  # number of data points

# Load Y values from CSV file
data = pd.read_csv('BSC_1_1_annotated.csv')
y = data['acc_x']  # Replace 'Y_column_name' with the actual column name in your CSV

for i in range(100):
    x.append(random.randint(0, 10))
    y.append(y[i])  # Append the next Y value from the CSV
    ax.plot(x, y, color='b')  # Plot X and Y values
    fig.canvas.draw()
    ax.set_xlim(left=max(0, i - 50), right=i + 3)
    time.sleep(0.01)

plt.show()