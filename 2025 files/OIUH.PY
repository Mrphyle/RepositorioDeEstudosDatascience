def avg():
    Heght = [1.90, 1.69, 1.53, 1.57, 1.66, 1.66, 1.76, 1.58, 1.81, 1.80, 1.75, 1.65, 1.75, 1.60, 1.64, 1.58, 1.75, 1.90, 1.78, 1.73, 1.83, 1.68, 1.84, 1.76, 1.65, 1.78, 2.13, 1.78]
    len_heght = len(Heght)
    media = sum(Heght)/len_heght
    print(media)
def center_number():
    Heght = [1.90, 1.69, 1.53, 1.57, 1.66, 1.66, 1.76, 1.58, 1.81, 1.80, 1.75, 1.65, 1.75, 1.60, 1.64, 1.58, 1.75, 1.90, 1.78, 1.73, 1.83, 1.68, 1.84, 1.76, 1.65, 1.78, 2.13, 1.78]
    Heght.sort()
    len_heght = len(Heght)
    center_number = len_heght/2
    if center_number.is_integer():
        second_number = int(center_number + 1)
        result = (Heght[int(center_number)] + Heght[second_number])/2
        print(f'a mediana par é {result:.2f}')
    else:
        number_float = (center_number - 0.5)
        print(f'{Heght[int(number_float)]:.2f}')
def moda():
    import pandas as pd
    Heght = [1.90, 1.69, 1.53, 1.57, 1.66, 1.66, 1.76, 1.58, 1.81, 1.80, 1.75, 1.65, 1.75, 1.60, 1.64, 1.58, 1.75, 1.90, 1.78, 1.73, 1.83, 1.68, 1.84, 1.76, 1.65, 1.78, 2.13, 1.78] 
    
     
    datas = pd.DataFrame(Heght)
    how_many = set(Heght)
    for i in how_many:
        number = Heght.count(i)    
    max_number = max(Heght)
    print(max_number, datas.mode())
def AVG_mediana_moda():
    import statistics as stats
    Heght = [1.90, 1.69, 1.53, 1.57, 1.66, 1.66, 1.76, 1.58, 1.81, 1.80, 1.75, 1.65, 1.75, 1.60, 1.64, 1.58, 1.75, 1.90, 1.78, 1.73, 1.83, 1.68, 1.84, 1.76, 1.65, 1.78, 2.13, 1.78]
    a= stats.median(Heght)
    b= stats.mode(Heght)
    c=stats.mean(Heght)
    print(a,b,c)
AVG_mediana_moda()