

import matplotlib.pyplot as plt 

y = [30.01,83.14,89.57,90.99]
x = [3.00,9.00,11.00,10.00]

plt.ylabel('Massa(g)')
plt.xlabel('ΔV(ml)')
plt.title("Gráfico Massa/ΔV (parte B)")
plt.axis(ymin=0, ymax=120)
plt.axis(xmin=0,xmax=14)
plt.grid(True)
plt.plot(x, y)
plt.plot(x,y,label = "Densidade ",marker ='o')
plt.legend()
plt.show()

plt.savefig('graficos.jpg',format = 'jpg')