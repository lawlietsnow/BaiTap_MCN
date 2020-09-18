import math
def tinhgiaithua(n):
    '''ád'''
    giai_thua = 1.0
    if (n == 0 or n == 1):
        return giai_thua
    else:
        for i in range(2, n + 1):
            giai_thua = giai_thua * i
        return giai_thua

def prob( n , m , p ):
    '''
    :param n: số thành công
    :param m: tổng số lần thử
    :param p: sắc xuẩt của 1 mặt
    :return:
    '''
    return (tinhgiaithua(m)/(tinhgiaithua(n)*tinhgiaithua(m-n)))*p**n*(1-p)**(m-n)

def infoMeasure( n,m , p):
    return -math.log2(prob(n,m,p))

def sumProb(n,m,p):
    sum=0
    for i in range(1,n+1):
        sum+=prob(i,m,p)
    return sum

def approxEntropy(n,m,p):
    entropy = 0
    for i in range(1,n+1):
        entropy+=prob(i,m,p)*infoMeasure(i,m,p)
    return entropy

