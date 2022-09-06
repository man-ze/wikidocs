# 161 0~99까지 한 라인에 하나씩 순차적으로 출력하는 프로그램 작성하기
for i in range(100):
  print(i)

# 162 range를 사용해서 2002~2050년까지 월드컵이 개최되는 년도만 출력 (4년에 한번)
# range의 세번 째 파라미터는 증감폭을 결정함
for i in range(2002, 2051, 4):
    print(i)

# 163 1부터 30까지의 숫자 중 3의 배수만 출력하기
for i in range(1, 31):
  if i%3 == 0:
    print(i)

# 164 99부터 0까지 1씩 감소하는 숫자들을, 한 라인에 하나씩 출력
for i in range(99, 0, -1):
     print(i)

# 165 for 문으로 0.0 ~ 0.9 까지 0.1 씩 증가시키기
for i in range(10):
  print(i/10)

# 166 구구단 3단 만들기
for i in range(1, 10):
  print("3x",i,"=",3*i)

print("-"*10)

# 167 3단에서 홀 수 번째만 출력하기
for i in range(1, 10, 2):
  print("3x",i,"=",3*i)

# 168 1~10 까지의 숫자를 모두 더한 값을 출력하기
  sum = 0
for i in range(1, 11):
  sum += i
  print(sum)

# 169 1~10 까지의 숫자 중 홀수의 합만 출력하기
  sum = 0
for i in range(1, 11, 2):
  sum += i
  print(sum)

# 170 1~10 까지의 숫자를 모두 곱한 값을 출력하기
  sum = 1
for i in range(1, 11):
  sum *= i 
  print(sum) 

print("="*20)

# 171 for 과 range 를 사용해서 리스트의 데이터를 출력하기
price_list = [32100, 32150, 32000, 32500]
for i in range(len(price_list)):
    print(price_list[i])

print("="*20)

# 172 for문과 range문을 사용해서 리스트의 인덱스번호와 데이터를 추출하기
# enumerate() 함수 : 인덱스와 원소를 동시에 접근하면서 loop 를 돌릴 수 있음 
price_list = [32100, 32150, 32000, 32500]
for i, data in enumerate(price_list):
    print(i, data)

print("="*20)


# 173 for문과 range문을 사용해서 리스트의 데이터를 추출 및 인덱스 역순으로 추출
for i in range(len(price_list)):
    print((len(price_list) - 1) - i, price_list[i])

print("="*20)

# 174 인덱스 번호를 100 부터 시작해서 출력하기
price_list = [32100, 32150, 32000, 32500] 
for i in range(1, 4):
    print(90 + 10 * i, price_list[i])

print("="*20)

# 175 아래처럼 출력하기 
"""
가 나
나 다
다 라
"""
my_list = ["가", "나", "다", "라"]
for i in [0, 1, 2]:
    print(my_list[i], my_list[i+1])

print("="*20)

for i in range( len(my_list)-1) :
  print(my_list[i], my_list[i+1])

# 176 아래처럼 출력하기
"""
가 나 다
나 다 라
다 라 마
"""

print("="*20)

my_list = ["가", "나", "다", "라", "마"]
for i in [0,1,2]:
  print(my_list[i], my_list[i+1], my_list[i+2])
  
print("="*20)

# 177 반복문과 range 함수를 사용해서 my_list를 아래와 같이 출력하기
"""
라 다
다 나
나 가
"""
my_list = ["가", "나", "다", "라"]
for i in [-1,-2,-3]:
  print(my_list[i], my_list[i-1])

print("="*20)

# 178 리스트 내부의 정수 연산 
# 리스트 요소에 우측 값 - 해당 인덱스 값 연산하여 출력하기
my_list = [100, 200, 400, 800]
for i in [0, 1, 2]:
    print(abs(my_list[i+1] - my_list[i]))

