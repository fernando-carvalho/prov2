import random
import matplotlib.pyplot as plt

volume = []
subpops = ['a','b','c','d','e','f','g']
safras = [201705,201706,201707,201708,201709,201710]
for subpop in subpops:
	volume_atual = []
	for safra in range(len(safras)):
		volume_atual.append(random.randint(0,100))
	volume.append(volume_atual)

print (volume)
	
cores = ['red','blue','orange','green','gray','yellow','pink']

fig = plt.figure(figsize=(20, 10))
ax = fig.add_subplot(1, 1, 1)

bottom = [0,0,0,0,0,0,0]
for i in range(len(volume)):
    for j in range(len(volume[i])):
            ax.bar(
                j,
                volume[i][j],
                bottom=bottom[j],
                color=cores[i],
		label=subpops[i],
                align='center',
            )
            bottom[j] += volume[i][j]

ax.set(xticks=range(len(safras)))
ax.set_xticklabels(safras)

# Put a legend below current axis
ax.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),
          fancybox=True, shadow=True, ncol=len(subpops))

#ax.set(xticks=safras)
#ax.set_xticklabels(safras)
#ax.xaxis.set_visible(False) 
#ax.yaxis.set_visible(False) 
#ax.set_xlabel('')
#ax.set_ylabel('')
plt.show()
