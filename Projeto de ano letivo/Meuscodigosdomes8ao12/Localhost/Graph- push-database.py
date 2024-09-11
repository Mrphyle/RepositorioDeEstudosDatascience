#localhost Obs:CREATE TABLE veiculos(id int PRIMARY KEY, marca varchar(50),modelo varchar(50))
import mysql.connector as mysql
import matplotlib.pyplot as plt
x = []
y= []
try:
    connect = mysql.connect(
        host = 'localhost',
        user= 'root',
        password = '',
        database = 'mrphyle',
    )
    sql = "SELECT modelo,COUNT(pessoas) FROM veiculos GROUP BY modelo ORDER BY pessoas;"
    cursor = connect.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for line in result:
        y.append(line[1])
        x.append(line[0])
except:
    print('ERROR!!')
finally:
    cursor.close()
    connect.close()
plt.style.use('dark_background')
cor = ['purple']
plt.bar(x,y,width=0.5,color=cor)
plt.title("quantidade de naves")
plt.show()
'''
import mysql.connector as mysql
import matplotlib.pyplot as plt
x = []
y= []
try:
    connect = mysql.connect(
        host = 'localhost',
        user= 'root',
        password = '',
        database = 'mrphyle',
    )
    sql = "SELECT marca, COUNT(marca) FROM veiculos GROUP BY marca;"
    cursor = connect.cursor()
    cursor.execute(sql)
    result = cursor.fetchall()
    for line in result:
        y.append(line[1])
        x.append(line[0])
except:
    print('ERROR!!')
cor = ['red','yellow','green']
plt.bar(x,y,width=0.5,color=cor)
plt.title("quantidade de naves")
plt.show()'''