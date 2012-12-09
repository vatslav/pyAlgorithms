#-------------------------------------------------------------------------------
# Name:        модуль1
# Purpose:
#
# Author:      Вацлав
#
# Created:     07.09.2012
# Copyright:   (c) Вацлав 2012
# Licence:     Public
#-------------------------------------------------------------------------------
from pprint import pprint
from tkinter import *
from tkinter.ttk import *
def main():
##    root = Tk()
##    f1, f1 = Frame(root), Frame(root)

    pprint(Pj(5,3,table))
a = (0.4, 0.25, 0.2, 0.1, 0.05)
b = (0,	0.35,0.3,0.25,0.1)
c = (0,	0, 0.45 ,0.4 ,0.15)
d = (0 ,0 ,0 ,0.4 ,0.6)
e = (0 ,0 ,0 ,0 ,1)
table = list((a,b,c,d,e))
##table = [list(x) for x in table]

#j - количество столбцов, к-строки
def Pj(j,k,t=table):

    if not t:return #если нефига нет, то аборт, но лучше конечно возбудить ошибку и потом словить ее
    for elem in t: #для строки в  таблице
        for x in elem: #для ячейки в строке
            try: float(x)
            except ValueError:
                return None
    #print()


    P = []       ##создаем список в котором будем хранить состояния системы
    P.append([not x or 0 for x in range(len(t[0])) ]) ##Так как до первого выстрела все объекты целы, то Р1(0)=1
    P.append([x for x in t[0]])   ##после 1-го выстрела все значения вероятностей соответствуют 1 строке матрицы переходных вероятностей
    pi = lambda k,i: P[k][i]          ##  вероятность i-го состояния системы после (k-1)-го шага, 1 отнимается перед вызывом
    ##т.к. тут тлько добавления к множеству нас не парит, что уже len(p)=2. НАчинаем с еденицы, чтобы не заместить 1-ый выстрел вторым.
    ##т.к. 1 выстрел уже смоделировн на 2 строки выше и его расчет тривиален
    for x in range(1,k): #для строк с 1 до к
        P.append([]) #добавляем строку в таблицу  результатов
        for J in range(j): # в каждой строки (j штук)
            P[x+1].append( sum( [pi(x,i) * t[i][J] for i in range(len(table))] ) )#умножение строки на столбец и суммирование, вродь :)
    return P
def myround(x):
    c = str (x)
    position = c.find('.')
    left = c[:position]
    right = c[position + 1 : position + 2]
    c5 = right.find('5') + 1
    c6 = right.find('6') + 1
    c7 = right.find('7') + 1
    c8 = right.find('8') + 1
    c9 = right.find('9') + 1
    return (int(left) + c5 + c6 + c7 + c8 + c9)


if __name__ == '__main__':
    main()
