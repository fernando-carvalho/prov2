
# coding: utf-8

# In[45]:


#https://www.kaggle.com/garethjns/microsoft-lightgbm-with-parameter-tuning-0-823/code


# In[79]:


def gera_folds(periodos_treino, folds_cv=5):
    
    folds = []
    
    tamanho_janela = len(periodos_treino) - folds_cv
    assert tamanho_janela > 0, 'Erro! O número de folds deve ser menor'+                              'que o número de meses do treino.'
    
    for i in range(folds_cv):
        
        fold_atual = {}
        fold_atual['treino'] = periodos_treino[i:i+tamanho_janela]
        fold_atual['teste'] = [periodos_treino[tamanho_janela + i]]
        
        print (i, fold_atual)
        
        folds.append(fold_atual)
        
    return folds
        


# In[80]:


import itertools

def gera_parametros():
    gridParams = {
            'boosting_type': ['gbdt'],
            'max_depth' : [-1,4,6],
            'objective': ['regression'], 
            'num_leaves': [10,25,50],
            'learning_rate': [0.005, 0.05, 0.5, 1],
            'max_bin': [512], 
            'subsample_for_bin': [200],
            'subsample' : [0.7,1],
            'subsample_freq': [1], 
            #'colsample_bytree' : [0.6, 0.8],
            'reg_alpha' : [1.5,5],
            'reg_lambda' : [5,10],
            'min_split_gain': [0.5], 
            #'min_child_weight': [1], 
            #'min_child_samples': [5], 
            #'scale_pos_weight': [1],
            #'num_class' : [1],
            'n_estimators': [10,25]
        }

    combinacoes = []
    lista_parametros = list(gridParams.keys())

    for valores in itertools.product(*[gridParams[x] for x in lista_parametros]):
        combinacao_atual = {}
        for i in range(len(valores)):
            combinacao_atual[lista_parametros[i]] = valores[i]
        combinacoes.append(combinacao_atual)

    print ('Num combinacoes:', len(combinacoes))
    return combinacoes


# In[81]:


# Gera base iris para testes

import pandas as pd
import random


base = pd.read_csv('iris.csv')


meses = []
for i in range(base.shape[0]):
        meses.append(random.randint(1,10))
base['mes'] = meses


variaveis_explicativas = ['var_1','var2','var_3','var_4']
variavel_resposta = 'classe'


# In[82]:


# Declaracao de quais periodos serao usados para treinmo e para teste
periodos = {}
periodos['treino'] = [1,3,4,5,6,7,8,9]
periodos['teste'] = [2,10]

# Gera os folds para uma validacao cruzada com janela deslizante
folds = gera_folds(periodos['treino'])
print (folds)

# Gera o vetor com todas as combinacoes de parametros
parametros = gera_parametros()


# ### Encontra os melhores parâmetros para o modelo

# In[83]:


import lightgbm as lgb
from sklearn.metrics import roc_auc_score


contagem_parametros = 0
resultados = []

melhor_resultado = 0
melhores_parametros = None

# Para cada combinacao de parametro
for parametros_atuais in parametros:
    
    contagem_parametros += 1
    resultados_cv = []
    print ('Processando combinação parâmetros', contagem_parametros)
    
    for i, fold in enumerate(folds):
        
        print ('\tRodando fold', i)
        
        X_treino = base[base['mes'].isin(fold['treino'])][variaveis_explicativas].values
        y_treino = base[base['mes'].isin(fold['treino'])][variavel_resposta].tolist()
        
        X_teste = base[base['mes'].isin(fold['teste'])][variaveis_explicativas].values
        y_teste = base[base['mes'].isin(fold['teste'])][variavel_resposta].tolist()
        
        modelo = lgb.LGBMClassifier(**parametros_atuais)
        modelo.fit(X_treino, y_treino)
        y_pred = modelo.predict(X_teste)
        
        resultados_cv.append(roc_auc_score(y_teste, y_pred))
        
    resultado_atual = resultados_cv.mean()
    
    if resultado_atual > melhor_resultado:
        melhor_resultado = resultado_atual
        melhores_parametros = parametros_atuais
    
    print ('Melhor resultado atual', melhor_resultado)
    
    resultados.append(resultado_atual)
    

