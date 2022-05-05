import numpy as np
import matplotlib.pyplot as plt 

x = np.array([0.85,0.78125,0.80869,0.781818,0.81666])
y = 1.255*x

plt.plot(x, y)
plt.xlabel('Variação de altura (h2/h1)(cm)')
plt.ylabel('Densidade do fluído (g/cm^3)')
plt.title("Gráfico ")
plt.axis(ymin=0.75, ymax=1.2)
plt.axis(xmin=0.75,xmax=0.9)
plt.grid(True)
plt.plot(x,y,label = "Densidade 1 ",marker ='o')
plt.legend()
plt.show()
plt.savefig('graficos.pdf',format = 'pdf')