drawer = ["양말", "속옷", "모자", "반팔", "바지"]

del drawer[3]
print(drawer)

drawer[3]=""
print(drawer)

drawer[3] = "점퍼"
print(drawer)


desk = list()
# 빈 리스트에 값을 추가하려면 append()를 이용한다.
# desk[0] = "book"
desk.append("book")
desk.append("양말")