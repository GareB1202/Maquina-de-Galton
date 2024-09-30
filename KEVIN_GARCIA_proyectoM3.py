import numpy as np
import matplotlib.pyplot as plt


bolitas=3000
niveles=12

array = np.zeros(niveles + 1, int)


def ObtenValor(bolitas, niveles):
    

    for i in range(niveles) :
        valor = np.random.random()
        if valor >= 0.5:
            bolitas+=1
        else:
            bolitas-=1

    return bolitas

for i in range(bolitas):
    valor=ObtenValor(0, niveles)
    indice= int((niveles + valor)/2)
    array[indice] +=1
    
print(array)

plt.plot(array)
plt.title("Maquina de Galton")
plt.xlabel("Niveles")
plt.ylabel("Bolitas")
plt.show()



   








