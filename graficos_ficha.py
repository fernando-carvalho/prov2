import matplotlib.pyplot as plt
import numpy as np

def escreve_legenda(ax, grupos, cores):
	for i in range((len(grupos)/2)):
		ax.text(0, 0.8-0.25*i, grupos[i], color=cores[i], fontsize=24)
	for i in range((len(grupos)/2)+1):
		j = i+len(grupos)/2
		ax.text(0.5, 0.8-0.25*i, grupos[j], color=cores[j], fontsize=24)
	ax.axis('off')

def plota_stacked(ax, dados, periodos, grupos, cores, legenda=False, ticks_x=False, titulo=False):

	posicoes = [0,0,0,0,0,0,0]
	for i in range(len(dados)):
	    for j in range(len(dados[i])):
		    ax.bar(
		        j,
		        dados[i][j],
		        bottom=posicoes[j],
		        color=cores[i],
			label=grupos[i],
		        align='center',
		    )
		    posicoes[j] += dados[i][j]

	if legenda:
		ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
		  	  fancybox=True, shadow=True, ncol=len(grupos))

	if ticks_x:
		ax.set(xticks=range(len(periodos)))
		ax.set_xticklabels(periodos)
		for tick in ax.get_xticklabels():
		    tick.set_rotation(-30)
	else:
		ax.xaxis.set_visible(False) 

	if titulo:
		ax.set_title(titulo)

	#ax.xaxis.set_visible(False) 
	#ax.yaxis.set_visible(False) 
	#ax.set_xlabel('')
	#ax.set_ylabel('')
	#return (ax)

def plota_linhas(ax, dados, periodos, grupos, cores, legenda=False, ticks_x=False, titulo=False):

	for i in range(len(dados)):
		for j in range(len(dados[i])):
		    ax.plot(
			periodos,
		        dados[i],
		        color=cores[i],
			label=grupos[i]
		    )

	if ticks_x:
		ax.set_xticklabels(periodos)
	else:
		ax.xaxis.set_visible(False) 
	if titulo:
		ax.set_title(titulo)


	for tick in ax.get_xticklabels():
	    tick.set_rotation(-30)


def plota_barras(ax, dados, periodos, grupos, cores, legenda=False, ticks_x=False, titulo=False):

	w = 0.1
	metade=int(len(grupos)/2)
	ind = np.arange(len(periodos))
	for i in range(len(dados)):
		for j in range(len(dados[i])):
		    ax.bar(ind+w*(i-metade), dados[i], width=w, color=cores[i], align='center')
		    

	if legenda:
		ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
		  	  fancybox=True, shadow=True, ncol=len(grupos))

	if ticks_x:
		ax.set(xticks=range(len(periodos)))
		ax.set_xticklabels(periodos)
		for tick in ax.get_xticklabels():
		    tick.set_rotation(-30)
	else:
		ax.xaxis.set_visible(False)
	if titulo:
		ax.set_title(titulo) 
