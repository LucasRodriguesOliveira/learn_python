from datetime import datetime


list = [1, 0, 0, 6, 3, 0, 7, 0, 3, 7, 1, 0]
list2 = list[:]

t = datetime.now()

for x in list:
  if x == 0:
    list.remove(x)
    list.append(x)

t2 = datetime.now()
print(list)
print(t2 - t)

t = datetime.now()

list3 = []
for i, x in enumerate(list2):
  if x == 0:
    list3.append(list2.pop(i))
  

t2 = datetime.now()

print(list2)
print(t2 - t)
