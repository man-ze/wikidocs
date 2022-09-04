# 리스트의 이해 []
# 내부에 문자와 숫자, 빈 자료형 모든 형태가 올 수 있다.
# +, * 연산이 가능하며 인덱스와 슬라이싱도 가능하다. 
# 수정과 삭제(del 함수)가 가능하다. 

# 리스트 요소 삽입 - append / insert 
# 리스트 확장 - extend 
# 리스트 요소 삭제 - del / remove / pop (삭제할 요소명)
# 리스트 내부의 요소 x 의 개수 세기 - count 


index = [1, 2, ["a", "b", ["Life", "is"]]]
print(index[2][-1][0])
print(index[0:2])
print(index[0:1])
print(index[0])
print(index[-1][1])

slice = [1,2,3,["a","b","c"],4,5]
print(slice[0:3])
print(slice[3:4])
print(slice[3][:2]) # 리스트 내부의 요소를 슬라이싱할때 ":"을 사용

# 리스트의 길이 구하는 함수 : len 
print(len(slice))

# 리스트의 수정
slice[1] = 7
print(slice) 

# 삭제는 del , remove 함수를 이용 
# def 변수명 [] or [:]

del slice[4]
print(slice)

# 051 리스트 만들기 
movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
print(movie_rank)

# 052 리스트에 "배트맨" 원소 추가하기 
# append 함수 : append()
movie_rank.append("배트맨")
print(movie_rank)

# 053 리스트 사이에 "슈퍼맨 요소 추가" 
# insert 함수 : insert(추가하고싶은 인덱스 번호, 추가할 요소)
movie_rank.insert(1, "슈퍼맨")
print(movie_rank)

# 054 리스트에서 '럭키'를 삭제하기 
# remove 함수 : remove() , 
# 같은 숫자(문자)가 여러개일경우 첫번째로 오는것만 삭제됨
movie_rank.remove("럭키")
# del movie_rank [3]
print(movie_rank)

# 056 lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를 모두 갖고 있는 langs 리스트 만들기

lang1 = ["C", "C++", "JAVA"]
lang2 = ["Python", "Go", "C#"]

langs = lang1+lang2
print(langs)

# 057 리스트에서 최댓값과 최솟값 출력하기
nums = [1, 2, 3, 4, 5, 6, 7]
print(max(nums))
print(min(nums))

# 058 리스트의 합계 출력
# sum : 리스트 내부의 요소의 합  
nums = [1, 2, 3, 4, 5]
print(sum(nums))

# 059 리스트에 저장된 데이터의 개수 구하기
cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
print(len(cook))

# 060 
nums = [1, 2, 3, 4, 5]
avr = sum(nums) / len(nums)
print(avr)

# 061 날짜 정보를 제외하고 가격 정보만을 출력하기
money = ['20180728', 100, 130, 140, 150, 160, 170]
print(money[1:])

# 062 홀수만 출력
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums[0:-1:2])

# 063 짝수만 출력
print(nums[1::2])

# 064 슬라이싱을 이용해서 역방향 출력하기
nums = [1, 2, 3, 4, 5]
print(nums[::-1])

# 065 문자열 여러개 출력 
many = ['삼성전자', 'LG전자', 'Naver']
print(many[0], many[2])

# 066 리스트 사이에 공백 넣어 출력하기 
# join 함수 : " ".join(변수명) / 문자열을 합치는 함수
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print(" ".join(interest))

# 067 리스트 사이에 "/" 넣어 출력하기
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("/".join(interest))

# 068 리스트 요소 개행하여 출력하기
interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
print("\n".join(interest))

# 069 "/" 없애고 각 단어를 분리해서 리스트로 저정하기
string = "삼성전자/LG전자/Naver"
print(string.split("/"))

# 070 리스트에 있는 값을 오름차순으로 정렬하기
# sort() : 오름차순 정렬 / reverse() : 내림차순정렬
data = [2, 4, 3, 1, 5, 10, 9]
data.sort()
print(data)
