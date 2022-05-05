import matplotlib.pyplot as plt 
import numpy as np

x = np. array([4.1,6.73,9.55,12.36])
y = np.array([0.040,0.065,0.093,0.12])


r = [4,6,9,12]
z = [0.0392,0.0587,0.0881,0.1175]

plt.ylabel('N')
plt.xlabel('Δv(cm^3))')
plt.title("Gráfico  (Corpo I)")
plt.axis(ymin=0, ymax=0.15)
plt.axis(xmin=0,xmax=15)

#plt.axis(rmin=0,rmax=15)
#plt.axis(zmin=0,zmax=0.15)
plt.grid(True)
plt.plot(x,y,label = "Peso_Vd ",marker ='o')
plt.plot(r,z,label = "Empuxo ",marker ='x')
plt.legend()
plt.show()

#plt.savefig('graficos.pdf',format = 'pdf')
