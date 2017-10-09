
# coding: utf-8

# In[36]:


def formata_valores(valor, porcentagem=False, 
                    casas_decimais=2,moeda=False):
    if moeda:
        return 'R$'+ str(int(valor))
    # Float
    if (isinstance(valor, float)):
        if porcentagem:
            valor *= 100
            return (f'{valor:.{casas_decimais}f}').replace('.',',')+'%'
        else:
            return (f'{valor:.{casas_decimais}f}').replace('.',',')
    # Inteiro
    if (isinstance(valor, int)):
        return str(valor)
    # String
    return valor


# In[40]:


valor = 23.4353545
f'{valor:.{5}f}'.replace('.',',')

