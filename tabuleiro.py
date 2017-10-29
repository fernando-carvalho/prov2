import matplotlib.pyplot as plt
import numpy as np


def plota_tabuleiro(ax, dados, cores, gruposx, gruposy):

	tabela = ax.table(cellText=dados,
                 rowLabels=gruposx,
                 colLabels=gruposy,
                 loc='center')
	tabela.set_fontsize(24)
	tabela.scale(0.8, 7)  
