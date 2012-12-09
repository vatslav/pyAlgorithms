__author__ = 'Вячеслав'

#рекурсивный НОД
superNod = lambda a,b: b and superNod (b, a%b) or a

#рекурсия, более читаьельная
def recnod(a, b):
    return b and recnod(b, a%b) or a

#циклический, в фп-стиле
def shortNod(a,b):
    while b!=0: a,b=b,a%b
    return a

#простой алгоритм
def simplenod(a,b):
    while a!=0 and b!= 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return a+b


if  __name__ ==  "__main__" :
    from random import randint
    rand = lambda:randint(5,100)
    print(simplenod(rand(),rand()) )
    print(superNod(rand(),rand() ))
    print(recnod(rand(),rand()))
    #тест показал, что нод НОД!=1 - редкость, надо будет проверить как ижет распределение НОДа на числах
