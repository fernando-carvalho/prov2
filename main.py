
# coding: utf-8

# In[1]:


from dados_basicos import Dados_basicos

infos = [
    {'campo':'volume',
     'valor':12345
    },
    {'campo':'br',
     'valor':0.345,
     'porcentagem':True,
     'casas_decimais':1
    },
    {'campo':'renda',
     'valor':283490,
    }
]

objeto = Dados_basicos(infos)
objeto.imprime_tabela()

