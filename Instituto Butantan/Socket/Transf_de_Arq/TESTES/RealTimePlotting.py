import matplotlib.pyplot as plt
import numpy as np

# Crie seus dados
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Crie a primeira figura
plt.figure(1)

# Primeiro gráfico
plt.subplot(211)  # 2 linhas, 1 coluna, primeiro gráfico
plt.plot(x, y1)
plt.title('Gráfico 1: Seno')

# Segundo gráfico
plt.subplot(212)  # 2 linhas, 1 coluna, segundo gráfico
plt.plot(x, y2)
plt.title('Gráfico 2: Cosseno')

# Ajuste de layout
plt.tight_layout()

# Exiba os gráficos
plt.show()