'''
num=int(input('Enter a number:'))
sum=0
i=1
while i<=num:
    sum=sum+i
    print('Sum in ',i,' is=',sum)
    i=i+1
#Break and continue
for i in range(6):
    if i==4:
        break
    print('B ',i)
for i in range(6):
    if i==4:
        continue
    print('C ',i)
'''
def myName(nam):
    '''this is documentation of this function'''
    print('My name is '+nam)
myName('FARHAD')
print(myName.__doc__)

print('----------')
def test():
    '''This function is about return statement'''
    x=10
    print(x)
    return x

print('--this will print the function--\n')
test()
print('\n')
print(test())