gender = input("성별을 입력하세요 : ")
grade = int(input("학년을 입력하세요 : "))

if gender=="남자" and grade==1:
    print("출입 허용")
else:
    print("출입 불가")