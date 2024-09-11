import matplotlib.pyplot as plt
x = [8,16,18]
Colors = ['purple','blue','green']
plt.figure(figsize=(8,8))
plt.pie(x,colors=Colors,autopct='%1.1f%%',startangle=0)
plt.title("18 is beatifull")
plt.show()