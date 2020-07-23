def gcd(x, y):
    while(y):
       x, y = y, x % y
    return x
     
     
def LCMofArray(a):
    l = a[0]
    for i in range(1,len(a)):
        l = l*a[i]//gcd(l, a[i])
    return l
     
     
T = input()
for w in range(int(T)):
    N, M, K = input().split()
    a = list(map(int,input().strip().split()))[:int(N)]
    lcm = LCMofArray(a)
    d = lcm % int(M)
    f = d ** int(K)
    g = f % int(M)
    print(g)
