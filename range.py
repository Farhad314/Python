print(range(10))
print(list(range(10)))
print(set(range(5)))

for i in range(6):
    print(i)
for i in range(1,11,2):
    print('##',i)

num=[3,8,5,12]
sum=0
for i in num:
    sum+=i
print('---sum=',sum)