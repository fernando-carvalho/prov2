
# coding: utf-8

# In[38]:


import matplotlib.pyplot as plt
import numpy as np
import formatacao

class Dados_basicos:
    '''
    Trata os dados basicos de um grupo de propostas
    Recebe um dicionario com as informacoes.
    Pode produzir uma tabela ou uma subfigura.
    '''
    
    def __init__(self, informacoes, tamanho):
        '''
        Informacoes deve ser um vetor de dicionario com
        os seguintes campos:
        [
            - campo
            - valor
            - porcentagem (opcional)
            - casas_decimais (opcional)
        ]
        '''
        self.informacoes = informacoes
        self.tamanho = tamanho
        
        
    def itera_informacoes(self):
        for informacao in self.informacoes:
            campo = informacao['campo']
            valor = informacao['valor']
            porcentagem = True if 'porcentagem'                 in informacao else None
            casas_decimais = informacao['casas_decimais']                 if 'casas_decimais' in informacao else None
            moeda = informacao['moeda']                 if 'moeda' in informacao else None
            yield campo,valor,porcentagem,casas_decimais,moeda
        
        
    def gera_subplot(self, ax):
        matriz_dados = []
        for campo,valor,porcentagem,casas_decimais,moeda                         in self.itera_informacoes():
            valor = formatacao.formata_valores(valor, 
                                  porcentagem=porcentagem, 
                                  casas_decimais=casas_decimais,
                                  moeda=moeda)
            matriz_dados.append([campo.title(), valor])
        tabela = ax.table(cellText=matriz_dados, loc='center')
        tabela.set_fontsize(self.tamanho)
        tabela.scale(1, 1.5)
    
        
    def imprime_tabela(self):
        for campo,valor,porcentagem,casas_decimais,moeda                         in self.itera_informacoes():
                valor = formatacao.formata_valores(valor, 
                                        porcentagem=porcentagem, 
                                        casas_decimais=casas_decimais,
                                        moeda=moeda)
                print (campo, valor)
                    

