# ********* 시험문제 **********
def profile(name, age, *language): # *language = language 인자의 갯수가 유동적이다
	print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
	for i in language:
		print(i, end=" ")
	print()
	
profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")
profile("백서진", 17, "C", "Python", "Java", "HTML", "CSS")