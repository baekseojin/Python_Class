# key 값은 중복 X, 수정도 안됨(불변타입) 


# 예제 1

# dic1 = {"apple":"사과", "bird":"새", "bug":"벌레"}
# print(dic1)

# dic2 = dict(apple = "사과", bird = "새", bug = "벌레")
# print(dic2)

# 예제 2

# dic1 = {"apple":"사과", "bird":"새", "bug":"벌레"}
# print(dic1)

# del dic1["bug"]
# print(dic1)

# 예제 3
# 중복 저장되지 않고 "num" : 4로 수정
dic = {"num":3}
dic["num"] = 4

dic[False] = 0

# value는 어느 값이든 저장 가능
dic[True] = [1, 10, 100]
dic["nums"] = {"one":1, "two":2}
print(dic)