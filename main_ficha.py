import random
import graficos
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

volume = []
subpops = ['Grupoa','Grupoab','Grupoac','Grupoad','Grupoae','Grupoaf','Grupoag']
safras = [201705,201706,201707,201708,201709,201710]
cores = ['red','blue','orange','green','gray','brown','pink']

for subpop in subpops:
	volume_atual = []
	for safra in range(len(safras)):
		volume_atual.append(random.randint(0,100))
	volume.append(volume_atual)


fig = plt.figure(figsize=(20, 12))
gs = gridspec.GridSpec(26, 40)
ax = [
      plt.subplot(gs[0:5, 0:20]),
      plt.subplot(gs[0:5, 20:40]),
      plt.subplot(gs[5:15, 0:10]),
      plt.subplot(gs[5:15, 10:20]),
      plt.subplot(gs[5:15, 20:30]),
      plt.subplot(gs[5:15, 30:40]),
      plt.subplot(gs[15:25, 0:10]),
      plt.subplot(gs[15:25, 10:20]),
      plt.subplot(gs[15:25, 20:30]),
      plt.subplot(gs[15:25, 30:40]),
      plt.subplot(gs[25:26, 0:40])]

ax[0].text(0.5, 0.5, s='parceria subpop', 
		horizontalalignment='center', 
		verticalalignment='center', 
		fontsize=30, 
		bbox={'facecolor':'lightblue', 'alpha':0.7, 'pad':50})
ax[0].axis('off')

graficos.escreve_legenda(ax[1], subpops, cores)
graficos.plota_stacked(ax[2], volume, safras, subpops, cores, titulo='Volume')
graficos.plota_linhas(ax[3], volume, safras, subpops, cores, titulo='Taxa aprovacao')
graficos.plota_barras(ax[4], volume, safras, subpops, cores, titulo='Idade media')
graficos.plota_linhas(ax[5], volume, safras, subpops, cores, titulo='Score V2 medio')
graficos.plota_linhas(ax[6], volume, safras, subpops, cores, ticks_x=True, titulo='Over 30 fisico')
graficos.plota_linhas(ax[7], volume, safras, subpops, cores, ticks_x=True, titulo='Over 30 financeiro')
graficos.plota_barras(ax[8], volume, safras, subpops, cores, ticks_x=True, titulo='Limite medio')
graficos.plota_barras(ax[9], volume, safras, subpops, cores, ticks_x=True, titulo='Renda media')
ax[10].axis('off')

plt.tight_layout()#pad=10, w_pad=7, h_pad=7)
#plt.show()
plt.savefig('teste.png')
