'''
sqr= lambda x: x*5
#this will store the function in square function
print(sqr(5))
'''
num=[1,2,3,4,5,6,7,8,9,10,11,12]
even=list(filter(lambda x:(x%2)==0,num))
#print('Even number=',even)

mul=tuple(map(lambda x:x*2,num))
print("Multiplication of 2=",mul)

'''x=45
def test():
    global x
    x=x+2
    print(x)
test()
'''