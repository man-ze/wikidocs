# 문자열의 연산

# 035 문자열 포매팅을 이용하여 아래처럼 출력
# 이름: 김민수 나이: 10
# 이름: 이철희 나이: 13

name1 = "김민수" 
age1 = 10
name2 = "이철희"
age2 = 13

print("이름: %s 나이: %s\n이름: %s 나이: %s" %(name1, age1, name2, age2))
print(f"이름: {name1} 나이: {age1}\n이름: {name2} 나이: {age2}")
print("이름: {0} 나이: {1}\n이름: {2} 나이: {3}".format(name1,age1,name2, age2))


# 039 '2020/03'만 출력 
분기 = "2020/03(E) (IFRS연결)"
print(분기[:7])

# 040 문자열의 좌우 공백 제거
data = "   삼성전자    " 
print(data.strip())

# 041 대문자 BTC_KRW로 변경
ticjer = "btc_krw"
print(ticjer.upper())

# 042 소문자 btc_krw로 변경
ticker = "BTC_KRW"
print(ticjer.lower())

# 043 문자열 'hello' 를 'Hello'로 변경
st = "hello"
print(st.capitalize())

# 044 endswith 메서드를 사용해서 파일 이름이 xlsx 로 끝나는지 확인하기
file_name = "보고서.xlsx"
print(file_name.endswith("xlsx"))

# 046 startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는지 확인하기
file_name = "2020_보고서.xlsx" 
print(file_name.startswith("2020"))

# 047 공백 기준으로 문자열 나누기
a = "hello world"
print(a.split(" "))

# 048 btc와 krw로 나누기
ticker = "btc_krw"
print(ticjer.split("_"))

# 049 연도/월/일 나누기
date = "2020-05-01"
print(date.split("-"))

# 050 오른쪽 공백 제거
data = "039490     "
print(data.rstrip())