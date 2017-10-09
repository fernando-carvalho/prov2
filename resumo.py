
# coding: utf-8

# In[23]:


import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np

from importlib import reload

import dados_basicos
reload(dados_basicos)
from dados_basicos import Dados_basicos

class Resumo:
    '''
    Cria uma imagem com o resumo do ensemble para 
    um par de parceria e subpop.
    Recebe como entrada as subfiguras prontas, o titulo e 
    configura a posição de cada subfigura na imagem final.
    '''
    
    def __init__(self, parceria, subpop, nome_arquivo, dados_basicos):
        '''
        eixos:  infos: resumo das informacoes
                swap: comparacao com outro modelo (matriz)
                gh_missing: resumo dos ghs da base sem missing
                gh_completos: resumo dos ghs da base com missing
                fluxo: informacao do fluxo de aprovacao
        '''
        #assert len(eixos) == 5, 'O numero de eixos passados deve ser 5!'      
        
        
        self.define_subfiguras() 
        self.preenche_titulo(parceria, subpop)
        self.preenche_dadosBasicos(dados_basicos)
        
        #self.atribui_subfiguras(eixos)
        self.remove_marcacoes()
        self.nome_arquivo = nome_arquivo
        #self.salva_imagem()
        
        
    def define_subfiguras(self):
        plt.figure(figsize=(15, 9))
        gs = gridspec.GridSpec(20, 30)
        self.eixos = [plt.subplot(gs[0:4,0:15]),
                      plt.subplot(gs[0:4,15:30]),
                      plt.subplot(gs[4:10,0:15]),
                      plt.subplot(gs[4:10,15:30]),
                      plt.subplot(gs[10:16,0:15]),
                      plt.subplot(gs[10:16,15:30]),
                      plt.subplot(gs[16:20,0:30])]

        
        
    def preenche_titulo(self, parceria, subpop):
        texto = parceria.replace('_', ' ').upper()
        texto += ' - ' + subpop.replace('_', ' ').upper()
        self.eixos[0].text(0.5, 0.5, texto,
                        verticalalignment='center', 
                        horizontalalignment='center',
                        color='#555555', fontsize=35)
        
    
    def preenche_dadosBasicos(self, dados):
        objeto = Dados_basicos(dados,16)
        objeto.imprime_tabela()
        objeto.gera_subplot(self.eixos[1])


    
    def remove_marcacoes(self):
        for eixo in self.eixos:
            eixo.set_xticks([])
            eixo.set_yticks([])
            eixo.set_xticklabels([])
            eixo.set_yticklabels([])
            #eixo.axis('off')
        
        
    def salva_imagem(self):
        plt.tight_layout()
        plt.show()
        #plt.savefig(self.nome_arquivo + '.png')
        
        

