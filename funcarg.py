def myTest(name='Alien',msg='ok'):
    #print(name,',',msg) if we use comma there'll be space after name,it's not case in +
    print(name+","+msg)

'''overriding in function,this func will print new argument
myTest('Farhad','very good')

this is executing by mentioning keyword
myTest(msg='Hello',name='Kevin')
'''
#Arbitrary Argument
def test(*msg):
    for i in msg:
        print('Farhad',i)

test('Hello!','How are you?','What are you  doing?')
