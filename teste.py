import sys
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def define_pontos_corte(dados, ids_linhas=None, ids_colunas=None,
						linhas_crescente=1, colunas_crescente=1, limite=17):
	cortes = []
	nega_todos = []

	# J eh a posicao onde ocorreu o primeiro valor desinquadrado em cada linha
	
	for i in range(len(dados)):

		nega_todos.append(dados[i][0] > limite)
		j = 0
		while dados[i][j] <= limite:
			j += 1
			if j == len(dados[i]):
				break
		cortes.append(j)
import sys
import random
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def define_pontos_corte(dados, ids_linhas=None, ids_colunas=None,
						linhas_crescente=1, colunas_crescente=1, limite=17):
	cortes = []
	nega_todos = []

	# J eh a posicao onde ocorreu o primeiro valor desinquadrado em cada linha
	
	for i in range(len(dados)):

		nega_todos.append(dados[i][0] > limite)
		j = 0
		while dados[i][j] <= limite:
			j += 1
			if j == len(dados[i]):
				break
		cortes.append(j)

	print nega_todos


	for i in range(1,len(cortes)):
		if cortes[i] > cortes[i-1]:
			cortes[i] = cortes[i-1]
	print cortes

	return cortes


dados = []
for i in range(7):
	lista = []
	for j in range(7):
		lista.append(random.randint(3+j*3+i*5,15+j*3+i*5))
	dados.append(lista)

for i in dados:
	print (i)
print()
cortes = define_pontos_corte(dados, limite=40)


import matplotlib.pyplot as plt
fig, ax = plt.subplots()
ax.matshow(dados, cmap=plt.cm.bwr)
for i in range(len(dados)):
	for j in range(len(dados[i])):
		ax.text(j, i, dados[i][j], va='center', ha='center')


for i in range(len(dados)):
	ax.plot([cortes[i]-0.5, cortes[i]-0.5], [(i)+0.5, (i)-0.5], 'k-', lw=3)
for i in range(len(dados)-1):
	ax.plot([cortes[i]-0.5, cortes[i+1]-0.5], [(i)+0.5, (i)+0.5], 'k-', lw=3)


ax.set_yticks([])
ax.set_xticks([])
plt.show()
