evennumbers = [2,4,6,8]
oddnumbers = [1,3,5,7]
print(evennumbers, oddnumbers) # [2,4,6,8] [1,3,5,7]

numbers = evennumbers + oddnumbers
print(numbers) # [2,4,6,8,1,3,5,7]

# sort와 sorted 차이점 알아두기 : sort는 정렬, sorted는 정렬 하지만 원본은 보존(print문 안에 쓰기)
numbers.sort() # 리스트 요소 순서대로 정렬
print(numbers) # [1,2,3,4,5,6,7,8]

print(sorted(evennumbers)) # 원본은 보존하고 print문에서만 정렬하고 싶을 때
print(evennumbers)

numbers.reverse() # 리스트의 순서를 반대로 뒤집는다
print(numbers) # [8,7,6,5,4,3,2,1]