numbers = []
print(numbers)

numbers.append(1)
numbers.append(7)
numbers.append(3)
numbers.append(6)
numbers.append(5)
numbers.append(2)
numbers.append(13)
numbers.append(14)
print(numbers)

# [:] : 리스트 전체를 가져옴
for i in numbers[:]:
   if i % 2 == 1:
      numbers.remove(i)
      
print(numbers)

numbers.insert(0, 20)
print(numbers)

numbers.sort()
print(numbers)