

import numpy as np
import matplotlib.pyplot as plt
import random 
 

repeticiones = 5 #cantidad de experimentos
iteraciones = 5000 #cantidad de tiradas

#crea listas bidimensional de dimension repeticiones x iteraciones

cont = [[0 for x in range(37)] for y in range(repeticiones)] #Cantidad de apariciones de cada número
ruleta = [[0 for x in range(iteraciones)] for y in range(repeticiones)] #Que números aparecieron en cada tirada
varianza = [[0 for x in range(iteraciones)] for y in range(repeticiones)] #Almacena la evolución de la varianza a través del tiempo
prom = [[0 for x in range(iteraciones)] for y in range(repeticiones)] #Almacena la evolución de la varianza a través del tiempo
numero = 17 #Número a analizar
n_cont = [[0 for x in range(iteraciones)] for y in range(repeticiones)] #Almacena la cantidad de apariciones del numero a través del tiempo

cont = np.array(cont, dtype=float) #tranformamos las lista en numpy arrays para aprovechar sus funciones
ruleta = np.array(ruleta, dtype=float)
varianza = np.array(varianza, dtype=float)
prom = np.array(prom, dtype=float)
n_cont = np.array(n_cont, dtype=float)




for j in range(repeticiones):
  for i in range(iteraciones):
      n = random.randint(0,36)
      cont[j][n] = cont[j][n] + 1
      ruleta[j][i] = n 
      if i>0:
        prom[j][i] = ruleta[j].sum() / (i+1)
        n_cont[j][i] = cont[j][numero + 1] / i
      else:
        prom[j][i] = ruleta[j][i]
        n_cont[j][i] = cont[j][numero + 1]
      varianza[j][i]= ruleta[j].var()



for i in range(repeticiones):
  plt.plot(range(0,iteraciones), n_cont[i])
plt.title('Frecuencia Relativa')
plt.ylabel("Frecuencia relativa")
plt.xlabel("Cantidad de tiradas")
plt.show()


for i in range(repeticiones):
  plt.plot(range(0,iteraciones), prom[i])
plt.title('Promedio')
plt.ylabel("Promedio")
plt.xlabel("Cantidad de tiradas")
plt.show()


for i in range(repeticiones):
  plt.plot(range(0,iteraciones), varianza[i])
plt.title('Varianza')
plt.ylabel("Varianza")
plt.xlabel("Cantidad de tiradas")
plt.show()

for i in range(repeticiones):
  plt.plot(range(0,iteraciones), np.sqrt(varianza[i]))
plt.title("Desvio estandar")
plt.ylabel("Desvio estandar")
plt.xlabel("Cantidad de tiradas")
plt.show()