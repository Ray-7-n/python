size = input('Select the size of the pizza (S/M/L): ')
bill=0
if size=='s' or size=='S':
    bill=bill+120
    print('the prize of the pizza will be',bill)
elif size=='m' or size=='M':
    bill=bill+150
    print('the prize of the pizza will be',bill)
elif size=='l' or size=='L':
    bill=bill+200
    print('the prize of the pizza will be',bill)

peperonies=input('Do you need peperonies (Y/N): ')
if (size=='s' or size=='S') and peperonies =='y' or peperonies =='Y':
    bill=bill+20
    
else:
    bill=bill+50
cheese=input('Do you need extra cheese?(y/n): ')
if cheese=="y" or cheese=="Y":
    bill=bill+30
    print('your total prize of a pizza will be: ',bill)
else:
    print('your total prize of a pizza will be: ',bill)


