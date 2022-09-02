# 문자열 인덱싱과 슬라이싱의 이해 

# 021 "p t" 출력 

letters = "python"
print(letters[0]+" "+letters[2])


# 022 뒤에 4자리만 출력 
license_plate = "24가 2210"
print(license_plate[-4:])

# 023 문자 "홀" 만 출력
# 문자열 슬라이싱에서 간격 설정하기 → [시작인덱스:마지막인덱스:출력간격]
string = "홀짝홀짝홀짝"
print(string[0:6:2])

# 024 문자열 거꾸로 뒤집어 출력하기
# 음의 간격 설정하기 → [:: 간격]
reverse = "PYTHON"
print(reverse[::-1])

# 025 하이픈을 공백으로 변경하기
phone_number = "010-1111-2222"
print(phone_number.replace("-", " "))

# 026 하이픈 없애기
phone_number = "010-1111-2222"
print(phone_number.replace("-", ""))

# 027 "kr" 만 출력하기 (도메인만 출력하기)

url = "http://sharebook.kr"
print(url[-2:])
 # ↓ 정확한 답 / splip() 안의 내용을 기준으로 문자열을 나눔
url_split = url.split('.')
print(url_split[-1])

# 028 소문자 a 를 대문자 A 로 변환하기
alph = 'abcdfe2a354a32a'
print(alph.replace("a","A"))