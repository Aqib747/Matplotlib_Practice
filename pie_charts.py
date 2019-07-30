from matplotlib import pyplot as plt
plt.style.use("fivethirtyeight")


# Language Popularity
slices = [59219, 55466, 47544, 36443, 35917]
labels = ['JavaScript', 'HTML/CSS', 'SQL', 'Python', 'Java']
explode = [0,0,0,0.1,0] # ----> to emphasise the pie of intrest 0.1 means 10% of the radius

# slices = [120,40,30,20]
# labels = ['sixty','forty','thirty','tweenty']
#colors = ['blue', 'red','green','yellow']

plt.pie(slices, labels= labels,shadow= True ,explode = explode,autopct="%1.0f%%", wedgeprops= {'edgecolor': 'black'})



plt.title("Programming Language Survey")
plt.tight_layout()
plt.show() 