import random
names=input('Enter the names seperated by commas: ')
h=names.split(',')
print(h)
y=list(h)
k=len(y)

z=random.randint(0,k-1)
print(f'{y[z]} wil pay the bill')