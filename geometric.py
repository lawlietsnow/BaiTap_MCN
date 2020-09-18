import math
def prob( n , p ):
    return ((1-p)**(n-1))*p

def infoMeasure( n , p):
    return -math.log2(prob(n,p))

def sumProb(n,p):
    '''
    ta có công thức cấp số nhân:
        nếu -1<q<1 thì Lim(n->vô cùng) Sn = u1/(1-q)
        với n là số thứ n
        u1 là số đầu tiền
        q công bội
    áp dụng:
        prob(vô cùng , p) = p/(1-(1-p)) = p/p = 1
    '''
    sum=0
    for i in range(1,n+1):
        sum+=prob(i,p)
    return sum

def approxEntropy(n,p):
    '''
    Với p = 0.5 thì approxEntropy(n,p) <= 2 (với mọi n)
    '''
    entropy = 0
    for i in range(1,n+1):
        entropy+=prob(i,p)*infoMeasure(i,p)
    return entropy

