# 141 리스트에 부가세 10% 포함된 가격을 for 문을 사용해 출력하기

list = [100, 200, 300]
for i in list:
  print(i + 10)

# 142 for 문 출력
menu = ["김밥", "라면", "튀김"]
for i in menu:
  print(i)

# 143 리스트 내부의 요소의 문자열 길이 반환
stock = ["sk하이닉스", "삼성전자", "lg전자"]
for i in stock:
  print(len(i))

# 144 for 문을 사용하여 동물의 첫 글자만 출력하기
animal = ['dog', 'cat', 'parrot']
for i in animal:
  print(i[0])

# 147 list 와 for 문을 이용하여 3단 출력
list = [1,2,3,4,5,6,7,8,9]
for i in list:
  print("3x",i,"=",3*i)

# 148 리스트 안의 네 개의 문자열 중 <나,다,라> 만 출력
hangul = ["가", "나", "다", "라"]
hangul = hangul[1:4]
for i in hangul:
  print(i)

# 149 리스트 안의 네 개의 문자열 중 <가,다> 만 출력
hangul = ["가", "나", "다", "라"]
hangul = hangul[:3:2]
for i in hangul:
  print(i)

# 150 문자열 역순으로 출력하기
hangul = ["가", "나", "다", "라"]
for i in hangul[::-1]:
  print(i)

# 151 for 문으로 리스트의 음수만 출력하기
negative = [3, -20, -3, 44]
for i in negative:
  if i < 0:
    print(i)

# 152 for 문으로 3의 배수만 출력하기
multiple = [3, 100, 23, 44]
for i in multiple:
  if i%3==0:
    print(i)

# 153 20 보다 작은 3의 배수만 출력
mult = [13, 21, 12, 14, 30, 18]
for i in mult:
  if i % 3 == 0 and i <20:
    print(i)

# 154 리스트에서 세 글자 이상인 문자만 화면에 출력하기
three = ["I", "study", "python", "language", "!"]
for i in three:
  if len(i) >= 3:
    print(i)

# 155 리스트에서 대문자만 화면에 출력하기
upper = ["A", "b", "c", "D"]
for i in upper:
  if i.isupper():
    print(i)

# 156 리스트에서 소문자만 화면에 출력하기
lower =  ["A", "b", "c", "D"]
for i in lower:
  if i.islower():
    print(i)

# 157 첫 글자를 대문자로 변환하여 출력
animal = ['dog', 'cat', 'parrot']
for i in animal:
  print(i.capitalize())

# 158 확장자를 제거하고 파일 이름만 화면에 출력
name = ['hello.py', 'ex01.py', 'intro.hwp']
for i in name:
  split = i.split(".")
  print(split[0])

# 159 확장자가 .h 인 파일을 출력하기
file = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in file:  
  if i.endswith(".h"):
    print(i)

# 160 확장자가 .h 나 .c 인 파일을 출력하기
fileName = ['intra.h', 'intra.c', 'define.h', 'run.py']
for i in fileName:
  if i.endswith(".c") or i.endswith(".h"):
    print(i)