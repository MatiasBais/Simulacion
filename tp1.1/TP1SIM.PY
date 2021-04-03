import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

hfont = {'fontname':'sans serif'}
plt.style.use('ggplot')
x_tiradas = 10000
n = 17
y = [0] * x_tiradas
frn = [0] * x_tiradas
fre = [1/37] * x_tiradas
a_y = np.array(y)
frec_relativa = np.array(np.zeros(x_tiradas))
promedio = np.array(np.zeros(x_tiradas))
desvio = np.array(np.zeros(x_tiradas))
varianza = np.array(np.zeros(x_tiradas))

for j in range(x_tiradas):
  if random.randint(0,37) == n:
    if j == 0:
      a_y[j] = 1
    else:
      a_y[j] = a_y[j-1] + 1
  else:
    a_y[j] = a_y[j-1]
  frec_relativa[j] = a_y[j] / x_tiradas
  promedio[j] = a_y.mean()
  varianza[j] = a_y.var()
  desvio[j] = a_y.std()

plt.plot(range(0,x_tiradas), frec_relativa, label ="frn", color ="red") 
plt.plot(range(0,x_tiradas), fre, label ="fre", color = "blue") 
plt.xlabel("Número de tiradas",**hfont) 
plt.ylabel("Frecuencia Relativa",**hfont)
plt.title('Frecuencia Relativa',**hfont)
plt.legend()
plt.show() #Muestra el gráfico

plt.plot(range(0,x_tiradas), promedio, label="vpn", color="red")
plt.plot(range(0,x_tiradas), [a_y.mean()] * x_tiradas, label ="vpe", color = "blue")
plt.xlabel("Número de tiradas",**hfont) 
plt.ylabel("Promedio",**hfont)
plt.title('Promedio',**hfont)
plt.legend()
plt.show()

plt.plot(range(0,x_tiradas), desvio, label="vd", color="red")
plt.plot(range(0,x_tiradas), [a_y.std()] * x_tiradas, label ="vde", color = "blue")
plt.xlabel("Numero de tiradas",**hfont) 
plt.ylabel("Desvío",**hfont)
plt.title('Desvío',**hfont)
plt.legend()
plt.show()

plt.plot(range(0,x_tiradas), varianza, label="vvn", color="red")
plt.plot(range(0,x_tiradas), [a_y.var()] * x_tiradas, label ="vve", color = "blue")
plt.xlabel("Número de tiradas",**hfont) 
plt.ylabel("Varianza",**hfont)
plt.title('Varianza',**hfont)
plt.legend()
plt.show()




##

y2 = [0] * x_tiradas
frn2 = [0] * x_tiradas
fre2 = [1/37] * x_tiradas
a_y2 = np.array(y)
frec_relativa2 = np.array(np.zeros(x_tiradas))
promedio2 = np.array(np.zeros(x_tiradas))
desvio2 = np.array(np.zeros(x_tiradas))
varianza2 = np.array(np.zeros(x_tiradas))


for i in range(5):
  for j in range(x_tiradas):
    if random.randint(0,37) == n:
      if j == 0:
        a_y2[j] = 1
      else:
        a_y2[j] = a_y2[j-1] + 1
    else:
      a_y2[j] = a_y2[j-1]
    frec_relativa2[j] = a_y2[j] / x_tiradas
    promedio2[j] = a_y2.mean()
    varianza2[j] = a_y2.var()
    desvio2[j] = a_y2.std()
  plt.plot(range(0,x_tiradas), frec_relativa2)
  y2 = [0] * x_tiradas
  frn2 = [0] * x_tiradas
  fre2 = [1/37] * x_tiradas
  a_y2 = np.array(y)
  frec_relativa2 = np.array(np.zeros(x_tiradas))
  promedio2 = np.array(np.zeros(x_tiradas))
  desvio2 = np.array(np.zeros(x_tiradas))
  varianza2 = np.array(np.zeros(x_tiradas))
  
  
plt.xlabel("Número de tiradas",**hfont) 
plt.ylabel("Frecuencia Relativa",**hfont)
plt.title('Frecuencia Relativa',**hfont)
plt.show() #Muestra el gráfico


##

y2 = [0] * x_tiradas
frn2 = [0] * x_tiradas
fre2 = [1/37] * x_tiradas
a_y2 = np.array(y)
frec_relativa2 = np.array(np.zeros(x_tiradas))
promedio2 = np.array(np.zeros(x_tiradas))
desvio2 = np.array(np.zeros(x_tiradas))
varianza2 = np.array(np.zeros(x_tiradas))


for i in range(5):
  for j in range(x_tiradas):
    if random.randint(0,37) == n:
      if j == 0:
        a_y2[j] = 1
      else:
        a_y2[j] = a_y2[j-1] + 1
    else:
      a_y2[j] = a_y2[j-1]
    frec_relativa2[j] = a_y2[j] / x_tiradas
    promedio2[j] = a_y2.mean()
    varianza2[j] = a_y2.var()
    desvio2[j] = a_y2.std()
  plt.plot(range(0,x_tiradas), promedio2)
  y2 = [0] * x_tiradas
  frn2 = [0] * x_tiradas
  fre2 = [1/37] * x_tiradas
  a_y2 = np.array(y)
  frec_relativa2 = np.array(np.zeros(x_tiradas))
  promedio2 = np.array(np.zeros(x_tiradas))
  desvio2 = np.array(np.zeros(x_tiradas))
  varianza2 = np.array(np.zeros(x_tiradas))
  
  
plt.xlabel("Número de tiradas",**hfont) 
plt.ylabel("Promedio",**hfont)
plt.title('Promedio',**hfont)
plt.show() #Muestra el gráfico

##


y2 = [0] * x_tiradas
frn2 = [0] * x_tiradas
fre2 = [1/37] * x_tiradas
a_y2 = np.array(y)
frec_relativa2 = np.array(np.zeros(x_tiradas))
promedio2 = np.array(np.zeros(x_tiradas))
desvio2 = np.array(np.zeros(x_tiradas))
varianza2 = np.array(np.zeros(x_tiradas))


for i in range(5):
  for j in range(x_tiradas):
    if random.randint(0,37) == n:
      if j == 0:
        a_y2[j] = 1
      else:
        a_y2[j] = a_y2[j-1] + 1
    else:
      a_y2[j] = a_y2[j-1]
    frec_relativa2[j] = a_y2[j] / x_tiradas
    promedio2[j] = a_y2.mean()
    varianza2[j] = a_y2.var()
    desvio2[j] = a_y2.std()
  plt.plot(range(0,x_tiradas), varianza2)
  y2 = [0] * x_tiradas
  frn2 = [0] * x_tiradas
  fre2 = [1/37] * x_tiradas
  a_y2 = np.array(y)
  frec_relativa2 = np.array(np.zeros(x_tiradas))
  promedio2 = np.array(np.zeros(x_tiradas))
  desvio2 = np.array(np.zeros(x_tiradas))
  varianza2 = np.array(np.zeros(x_tiradas))
  
  
plt.xlabel("Numero de tiradas",**hfont) 
plt.ylabel("Desvío",**hfont)
plt.title('Desvío',**hfont)
plt.show() #Muestra el gráfico


###

y2 = [0] * x_tiradas
frn2 = [0] * x_tiradas
fre2 = [1/37] * x_tiradas
a_y2 = np.array(y)
frec_relativa2 = np.array(np.zeros(x_tiradas))
promedio2 = np.array(np.zeros(x_tiradas))
desvio2 = np.array(np.zeros(x_tiradas))
varianza2 = np.array(np.zeros(x_tiradas))


for i in range(5):
  for j in range(x_tiradas):
    if random.randint(0,37) == n:
      if j == 0:
        a_y2[j] = 1
      else:
        a_y2[j] = a_y2[j-1] + 1
    else:
      a_y2[j] = a_y2[j-1]
    frec_relativa2[j] = a_y2[j] / x_tiradas
    promedio2[j] = a_y2.mean()
    varianza2[j] = a_y2.var()
    desvio2[j] = a_y2.std()
  plt.plot(range(0,x_tiradas), desvio2)
  y2 = [0] * x_tiradas
  frn2 = [0] * x_tiradas
  fre2 = [1/37] * x_tiradas
  a_y2 = np.array(y)
  frec_relativa2 = np.array(np.zeros(x_tiradas))
  promedio2 = np.array(np.zeros(x_tiradas))
  desvio2 = np.array(np.zeros(x_tiradas))
  varianza2 = np.array(np.zeros(x_tiradas))
  
  
plt.xlabel("Número de tiradas",**hfont) 
plt.ylabel("Varianza",**hfont)
plt.title('Varianza',**hfont)
plt.show() #Muestra el gráfico

