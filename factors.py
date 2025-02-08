roll= int(input('Enter: '))
def factor(a):
    f=0
    k=0
    j=0
    for i in range(1,a+1):
        if a%i==0:
            f=f+1    
            if i%2==0:
                k=k+1
            if i%2!=0:
                j=j+1
    return f,k,j
   
print(factor(roll))

