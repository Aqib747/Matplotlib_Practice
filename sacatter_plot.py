import pandas as pd
from matplotlib import pyplot as plt
#scatter plot is used to show correlation
plt.style.use("seaborn")

data = pd.read_csv('2019-05-31-data.csv')
view_count = data['view_count']
likes = data['likes']
ratio = data['ratio']

plt.scatter(view_count, likes,c=ratio,cmap='summer' ,edgecolor='black', linewidth=1, alpha=0.75) #cmap = is color map style

cbar = plt.colorbar() # this will set the sliding table of color contrast
cbar.set_label('like dislike ratio')

plt.xscale("log") #----------> from this data will not clutter at one place
plt.yscale("log")

plt.title('Trending YouTube Videos')
plt.xlabel('View Count')
plt.ylabel('Total Likes')

plt.tight_layout()

plt.show()
