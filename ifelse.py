a=-5
if a>0:
    print('a=',a)
num=int(input('Enter a number '))
if num>0:
    print('This is positive number')
elif num==0:
    print ('zero')
else:
    print('This is negative number')
#nested    
num=int(input('Enter a number '))
if num>=0:
    if (num%2)==0:
        print('This is even number')
    else:
        print('This is odd number')
else:
    print ('This is negative number')
