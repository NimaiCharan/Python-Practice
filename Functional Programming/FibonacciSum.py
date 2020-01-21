def fibo_sum(n):
    a=0
    b=1
    sum=a+b
    print(a,b)
    for i in range(2,n):
        c=a+b
        a=b
        b=c
        sum=sum+c
        print(c)
    print(sum)
fibo_sum(5)
    
