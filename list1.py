grocery_item=['rice','soda','atta']
print(grocery_item)
#append method will add an item behind the list
grocery_item.append("water")
print(grocery_item)
#access index
#grocery_item=['rice','soda','atta',10]
print(grocery_item[1])
print(grocery_item[-1])
#data type & certain index
print('Type of classs',type(grocery_item))
print(grocery_item[1:3])
#sorting a list
grocery_item.sort()
print("Sorted list- ",grocery_item)
