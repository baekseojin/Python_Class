# *********시험문제**********
def profile(name, age, lang1, lang2, lang3, lang4, lang5):
	print("이름 : {0}\t나이 : {1}\t".format(name, age), end=" ")
	print(lang1, lang2, lang3, lang4, lang5)
	
profile("유재석", 20, "Python", "Java", "C", "C++", "C#")
profile("김태호", 25, "Kotlin", "Swift", "", "", "")
profile("백서진", 17, "C", "Python", "Java", "HTML", "CSS")