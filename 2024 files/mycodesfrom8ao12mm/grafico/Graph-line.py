import matplotlib.pyplot as plt
x = [18,20,26,28]
y = [16,14,15,17]
plt.plot(x,y,marker='o',linestyle='-',color='b',label='Datas')
plt.title("18 is beatifull")
plt.xlabel('X')
plt.ylabel("Y")
plt.legend()
plt.grid(True)
plt.show()