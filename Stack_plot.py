from matplotlib import pyplot as plt

plt.style.use("fivethirtyeight")

minutes = [1, 2, 3, 4, 5, 6, 7, 8, 9]

player1 = [1, 2, 2, 4, 4, 4, 4, 5 ,5]
player2 = [1, 1, 1, 1, 1, 2, 2, 2 ,4]
player3 = [1, 2, 2, 3, 3, 3, 3, 3 ,3]

labels = ['player1','player2','player3']

#plt.pie([1,1,1], labels= ['player1','player2','player3'])
plt.stackplot(minutes, player1, player2, player3,labels = labels)

plt.legend(loc="upper left")
plt.title("This a tut on stack plot")
plt.tight_layout()
plt.show()