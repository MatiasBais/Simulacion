import numpy as np
import matplotlib.pyplot as plt
import random 
 
iteraciones = 5000 #cantidad de tiradas
cont = np.array(np.zeros(37))
ruleta = np.array([])
varianza = np.array(np.zeros(iteraciones))
prom = np.array(np.zeros(iteraciones))
numero = 17
n_cont = np.array(np.zeros(iteraciones))
 
for i in range(iteraciones):
    n = random.randint(0,36)
    cont[n] = cont[n] + 1
    ruleta = np.append(ruleta,[n]) 
    if i>0:
      prom[i] = ruleta.sum() / (i+1)
      n_cont[i] = cont[numero + 1] / i
    else:
      prom[i] = ruleta.sum()
      n_cont[i] = cont[numero + 1]
    varianza[i]= ruleta.var()


plt.plot(range(0,iteraciones), n_cont, color="red")
plt.title('Frecuencia Relativa')
plt.ylabel("Frecuencia relativa")
plt.xlabel("Cantidad de tiradas")
plt.show()

plt.plot(range(0,iteraciones), prom, color="red")
plt.title('Promedio')
plt.ylabel("Promedio")
plt.xlabel("Cantidad de tiradas")
plt.show()


plt.plot(range(0,iteraciones), varianza, color="red")
plt.title('Varianza')
plt.ylabel("Varianza")
plt.xlabel("Cantidad de tiradas")
plt.show()

plt.plot(range(0,iteraciones), np.sqrt(varianza), color="red")
plt.title('Desvio estandar')
plt.ylabel("Desvio estandar")
plt.xlabel("Cantidad de tiradas")
plt.show()
