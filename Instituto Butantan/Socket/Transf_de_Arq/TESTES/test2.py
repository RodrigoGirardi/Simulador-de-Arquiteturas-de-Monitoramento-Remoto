import matplotlib.pyplot as plt

# Criar uma figura com 2 linhas e 2 colunas de subplots
plt.subplot(2, 2, 1)  # Primeiro subplot
plt.plot([1, 2, 3, 4], [1, 2, 3, 4])

plt.subplot(2, 2, 2)  # Segundo subplot
plt.scatter([1, 2, 3, 4], [4, 3, 2, 1])

plt.subplot(2, 2, 3)  # Terceiro subplot
plt.bar(['A', 'B', 'C', 'D'], [3, 5, 2, 7])

plt.subplot(2, 2, 4)  # Quarto subplot
plt.pie([2, 3, 4, 1], labels=['A', 'B', 'C', 'D'], autopct='%1.1f%%')

plt.show()