# 튜플의 이해 ()

# 튜플과 리스트의 차이점? 
# (1) 튜플은 내부의 요소가 하나뿐일지라도 반드시 ","로 구분해줘야만 한다.
# (2) 튜플은 리스트와는 달리 () 생략이 가능하다.
# ★ (3) 튜플은 한 번 생성하면 그 값을 변경할 수 없다. 

# 튜플과 리스트의 공통점?
# 위의 내용을 제외하면 리스트와 동일하므로 인덱싱, 슬라이싱, 연산이 가능함

# 071 my_variable 이름의 비어있는 튜플 만들기
from cgi import print_arguments


my_variable = ()
print(type(my_variable), my_variable)

# 072 movie_rank 라는 튜플을 생성하라
movie_rank = ("닥터 스트레인지", "스플릿", "럭키")
print(movie_rank)

# 073 숫자 1 이 저장된 튜플 생성
num1 = (1,)
print(type(num1))

# 077 튜플을 리스트로 변환하라.
interest = ('삼성전자', 'LG전자', 'SK Hynix')
print(list(interest))

# 080 1부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
data = tuple(range(2, 100, 2))
print( data )

# for i in range(1, 100):
#   if(i%2==0):
#     print(i)





