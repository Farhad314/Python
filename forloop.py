a=127
print ( a)
for i in range(1,5):
    print (i)
print('What')
b='1st string'
print(b)

c=6
print(c,'is the type of',type(c))
c=6.34
print(c,'is the type of',type(c))
c=6+1j
print(c,'is the type of',type(c))

#input method
x=input('Enter a number:')
print('number',x)
#adding
x=input('X=')
y=input('Y=')
z=int(x)+float(y)
print('sum of X,Y = ',z)
# importing from another file
import list
print(list.l[2])