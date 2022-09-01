import matplotlib.pyplot as plt

plt.scatter([1,2,3,4],[1,2,3,4])
plt.ylabel('Eixo Y')
plt.xlabel('Eixo X')
plt.title('Novo Gráfico')
plt.xticks([0,1,2,3,4,5,6])
plt.yticks([0,2,4,6])
plt.legend()
plt.show()
