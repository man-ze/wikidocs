# 111 사용자로부터 입력받은 문자열을 두 번 출력하기

user = input("문자를 입력하세요:")
print(user * 2)

# 112 사용자로부터 숫자 하나를 입력받고, 그 숫자에 10을 더해 출력하기
# input() 은 입력되는 모든것을 문자열로 취급하기 때문에, 숫자연산을 하고 싶을 때는 형변환을 해야함

num = input("숫자를 입력하세요:")
print(int(num) + 10)

# 113 사용자로부터 하나의 숫자를 입력 받고 짝수/홀수를 판별하기

num = input("숫자를 입력하세요: ")
if int(num) % 2 == 0 :
  print("짝수 입니다.")
else:
  print("홀수 입니다.")

# 114 사용자로부터 입력받은 값에 20을 더한 값을 출력 (단, 255를 넘는 경우 255를 출력함)

# num = input("숫자를 입력하세요")
# if int(num)+20 <= 255: 
#   print(int(num)+20)
# else:
#   print(255)

user = input("입력값: ")
num = 20 + int(user)
if num > 255:
  print(255)
else:
  print(num)

# 115 사용자로부터 입력받은 값에 20을 뺀 값을 출력 (단, 출력 범위는 0~255 사이의 값으로 결과가 0보다 작으면 0을 출력하고 255를 넘으면 255를 출력함)

user = input("숫자를 입력하세요: ")
num = int(user)-20
if num < 0:
  print(0) 
elif num > 255:
  print(255)
else:
  print(num) 

# 116 사용자로부터 입력 받은 시간이 정각인지 판별하기
hour = input("현재시간: ")
if hour[-2:] == "00":
    print("정각 입니다.")
else:
    print("정각이 아닙니다.")

# 117 사용자로 입력받은 단어가 fruit 리스트에 포함되어 있는지 확인
fruit = ["사과", "포도", "홍시"]
user = input("단어를 입력해보세요: ")
if user in fruit:
  print("해당 단어가 리스트에 있습니다.")
else:
  print("해당 단어는 리스트에 없습니다.")

# 118 사용자로부터 종목명을 입력받아, 리스트에 포함되어 있는지 확인 
warn_investment_list = ["Microsoft", "Google", "Naver", "Kakao", "SAMSUNG", "LG"]
user = input("종목명: ")
if user in warn_investment_list:
  print("투자 경고 종목 입니다.")
else:
  print("투자 경고 종목이 아닙니다.")   

# 119 사용자가 입력한 값이 딕셔너리 key 값에 포함되었는지 확인
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("계절: ")
if user in fruit.keys():
  print(user + "값은 딕셔너리의 key 값이 맞습니다.")
else:
  print(user + "값은 딕셔너리의 key 값이 아닙니다.")

# 120 사용자가 입력한 값이 딕셔너리 value 값에 포함되었는지 확인
fruit = {"봄" : "딸기", "여름" : "토마토", "가을" : "사과"}
user = input("과일: ")
if user in fruit.values():
  print(user + "값은 딕셔너리의 value 값에 해당됩니다.")
else: 
  print(user + "값은 딕셔너리의 value 값이 아닙니다.")

# 121 사용자로부터 입력받은 문자 하나를 소문자는 대문자로, 대문자는 소문자로 변경해서 출력하기
user = input()
if user.islower():
  print(user.upper())
else:
  print(user.lower())

# 124 사용자로부터 세 개의 숫자를 입력 받은 후 가장 큰 숫자 출력하기
user1 = input("첫번째 숫자: ")
user2 = input("두번째 숫자: ")
user3 = input("세번째 숫자: ")
user1 = int(user1)
user2 = int(user2)
user3 = int(user3)

if user1 >= user2 and user1 >= user3:
  print(user1)
elif user2 > user1 and user2 > user3:
  print(user2)
else:
  print(user3)

# 127 사용자로부터 13자리의 주민번호를 입력받아 성별을 확인하는 프로그램을 만들기

user = input("주민번호를 입력해주세요: ")
jumin = user[7]

if jumin == 2 or 4:
  print("여성")
else:
  print("남성") 