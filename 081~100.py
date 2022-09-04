# 딕셔너리의 이해 {key:value, key:value, ...}

# 딕셔너리는 리스트나 튜플과는 다르게 key 값을 통해 value 를 매칭한다.

# value 는 불변값/가변값/리스트 모두 사용 가능하다.
# key 는 불변/고정값이므로 중복되는 값이 있을 경우 한가지만 처리한다.
# key 는 불변/고정되는 자료형만 올 수 있다. (리스트x, 튜플o)

# 딕셔너리에 key:value 쌍 추가

a = {1: "a"}
a[2] = "b"
a["language"] = "python"
print(a)

# 딕셔너리 요소 삭제 (del)
del a[1]
print(a)

# 딕셔너리 value 값 얻기
print(a["language"])

# keys() : 딕셔너리의 key만 모아서 dict_keys 라는 객체로 반환 
a = {"name":"pey", "phone":"01199993323", "birth":"1118"}
print(a.keys())

# values() : 딕셔너리의 value만 모아서 dict_values 라는 객체로 반환
a = {"name":"pey", "phone":"01199993323", "birth":"1118"}
print(a.values())

# items() : key 와 value 를 쌍으로 묶어 튜플로 출력
print(a.items())

# 딕셔너리의 쌍 지우기
# 빈 딕셔너리는 {} 로 표현 / 새로 생성하려면 a = dict() 로 생성.
a.clear()
print(a) 

# 딕셔너리에서 key 추출할 때
a = {"name":"pey", "phone":"01199993323", "birth":"1118"}
print(a["name"])
print(a.get("name"))


# 해당 key 가 딕셔너리 안에 있는지 조사하기 (in)
a = {"name":"pey", "phone":"01199993323", "birth":"1118"}
print("name" in a) # true

# 085 딕셔너리 생성
icecream = {"메로나":1000, "폴라포":1200, "빵빠레":1800}
print(icecream)

# 086 딕셔너리에 가격정보 추가하기
# icecream = ["죠스바"] = 1200
# icecream = ["월드콘"] = 1500

print(icecream)

# 087 메로나 가격 출력
print(icecream["메로나"])

# 088 메로나 가격을 1300 으로 수정
icecream["메로나"] = 1300
print(icecream)

# 089 메로나 삭제하기
del icecream ["메로나"]
print(icecream)

# 091 리스트를 value 로 가지는 딕셔너리 생성
inventory = {"메로나":[300, 20], "비비빅":[400, 3], "죠스바":[250, 100]}
print(inventory)

# 092 inventory 딕셔너리에서 메로나의 가격을 화면에 출력
print(inventory["메로나"][0],"원")

# 093 inventory 딕셔너리에서 메로나의 재고를 화면에 출력
print(inventory["메로나"][1], "개")

# 094 딕셔너리에 새로운 딕셔너리 추가하기
inventory["월드콘"] = [500, 7]
print(inventory)

# 095 key 값으로만 구성된 리스트를 생성
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
ice = list(icecream.keys()) # dict_key 객체가 아닌 list 형태로 반환 
print(ice)

# 096 values 값으로만 구성된 리스트를 생성
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
cream = list(icecream.values())
print(cream)

# 097 icecream 딕셔너리에서 아이스크림 판매 금액의 총합 출력하기
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000} 
print(sum(cream), "원")

# 098 new_product 딕셔너리를 icecream 딕셔너리에 추가
# update 함수 : 딕셔너리에 신규 딕셔너리를 확장함 (리스트의 extend 와 유사)
icecream = {'탱크보이': 1200, '폴라포': 1200, '빵빠레': 1800, '월드콘': 1500, '메로나': 1000}
new_product = {'팥빙수':2700, '아맛나':1000} 
icecream.update(new_product)
print(icecream)

# 099 튜플을 하나의 딕셔너리로 변환하기 
# zip 함수 : key 와 value 를 분류해서 출력
keys = ("apple", "pear", "peach")
vals = (300, 250, 400)

result = dict(zip(keys, vals))
print(result)

# 100 date와 close_price 두 개의 리스트를 close_table 이름의 딕셔너리로 생성
date = ['09/05', '09/06', '09/07', '09/08', '09/09']
close_price = [10500, 10300, 10100, 10800, 11000]
close_table = dict(zip(date, close_price))
print(close_table)