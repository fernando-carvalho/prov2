import random
import tabuleiro
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

volume = []
subpops = ['Grupoa','Grupoab','Grupoac','Grupoad','Grupoae','Grupoaf','Grupoag']
ghs = ['GH1','GH2','GH3','GH4','GH5','GH6','GH7']
cores = []

for subpop in subpops:
	volume_atual = []
	for gh in range(len(ghs)):
		volume_atual.append(str(random.randint(0,100)) + '\n' + 'Volume')
	volume.append(volume_atual)


fig = plt.figure(figsize=(20, 12))
#fig.patch.set_visible(False)
gs = gridspec.GridSpec(21, 40)
ax = [
      plt.subplot(gs[0:1, 0:40]),
      plt.subplot(gs[1:21, 0:40])]

ax[0].text(0.5, 0.5, s='parceria subpop', 
		horizontalalignment='center', 
		verticalalignment='center', 
		fontsize=30, 
		bbox={'facecolor':'lightblue', 'alpha':0.7, 'pad':50})
ax[0].axis('off')

tabuleiro.plota_tabuleiro(ax[1], volume, cores, subpops, ghs)
ax[1].axis('off')

plt.tight_layout()#pad=10, w_pad=7, h_pad=7)
#plt.show()
plt.savefig('teste.png', dpi=300)
