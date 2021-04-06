def is_even(num):
    if num%2==0:
        return True
    else:
        return False

n=0
even=[]
while n<=100:
    if is_even(n):
        even.append(n)

        '''
        print(f"{n} is even")
    else:
        print(f"{n} is odd")
    '''
    n=n+1
print("Even number=",even)
grocery_item=['rice','soda','atta','water','water','pen']
for item in grocery_item:
    if item=='atta':
        continue #break
    print(item)
for i in range(0,len(grocery_item)):
    print(grocery_item[i],end='')