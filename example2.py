import matplotlib.pyplot as plt
activities=['eat','sleep','work','play']
slices=[3,7,8,6]
colors=['r','m','g','b']
plt.pie(slices,labels=activities,colors=colors,startangle=90,explode=(0.1,0,0,0),shadow=True,autopct='81.2f88')
plt.legend()
plt.show()
