################################################################################################################################
# 작성일 : 2024년 5월 1일
# 파일명 : print 테스트
# 개발자 : 장국진
# 사용 라이브러리 : request
################################################################################################################################
'''
주석 종류
'''

# 주석 처리 --> 블럭 선택 후 ctrl + /

# 문자 출력
print("테스트1")
print('테스트2')

# 숫자 출력
print(5+4)

# 변수
# test_var = "var테스트" (X) ------> 카멜 습관화 ↓
testVar = "var테스트"
print(testVar)

# 전역변수 --> 앞에 G 포함
G_TESTVAR = "11"
gTestVar = "22"

# Python Type
age = 26
print(age)
print(type(age))

# 입력

# iTest = input("숫자를 입력하세요: ")
# print("입력된 숫자는 " + iTest + " " + iTest + "입니다." )
# print(iTest)
# print(type(iTest))

# # fstring
# print(f"입력된 숫자는 {iTest} {iTest} 입니다." )
# # 여러줄
# print(f"""입력된 숫자는 {iTest} {iTest} 입니다.
# 테스트 입니다. {iTest}
# """ )

# 실수
pi = 3.14
print(pi)
print(type(pi))

# 실수 계산 방법
pi = 3.141592654
# 		 123456789
round_pi = round(pi, 5)
print(round_pi)

# 정수 -> 실수
aa = 1
print(aa)
print(type(aa))

aa = 1.
print(aa)
print(type(aa))

