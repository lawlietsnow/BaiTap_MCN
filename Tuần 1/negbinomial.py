from binomial import tinhgiaithua
import math
def prob( n ,m ,p ):
    '''
        :param n: tổng số thành công mong muốn
        :param m: tổng số lần thử
        :param p: sắc xuẩt của 1 mặt
        :return:
    '''
    return (tinhgiaithua(m-1)/(tinhgiaithua(m-n)*tinhgiaithua(n-1)))*(p**n)*((1-p)**(m-n))

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

