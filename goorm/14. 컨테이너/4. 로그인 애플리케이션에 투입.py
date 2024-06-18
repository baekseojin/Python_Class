input_id = input("아이디를 입력해주세요.\n")
ids = ['egoing', 'k8805', 'leezche']
for id in ids:
    if id == input_id:
        print('Hello!, '+id)
        import sys 
        sys.exit() # 프로그램 완전 종료 != break
print('Who are you?')