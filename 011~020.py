# 파이썬 변수와 형변환의 이해

# 015 type 함수
a = "132"
print(type(a))

# 016 문자열을 정수로 변환
num_str = "720"
num_str = int(num_str)
print(num_str, type(num_str))

# 017 정수를 문자열 100으로 변환
num = 100
num = str(num)
print(num, type(num))

# 018 문자열을 실수로 변환 
a = 15.79
a = float(15.79)
print(a, type(a))

# 019 문자열을 정수로 변환
# year 를 정수로 변환한 후 최근 3년의 연도를 화면에 출력하기
year = "2022"
year = int(year)

three = 0
while three <= 2 :
  three += 1
  print((year+1)-three)

'''에이컨이 월 48,584원에 무이자 36개월의 조건으로 홈쇼핑에서 판매될 때 총 금액을 계산한 후 이를 화면에 출력하기 '''

aircon = 48584
print("총 가격은" + str(aircon*36) + "원 입니다.")

