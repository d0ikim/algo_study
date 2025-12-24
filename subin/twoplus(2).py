numbers = [5, 0, 2, 7]
#numbers = list(map(int, input("정수 입력: ").split()))

#2-2) 두 숫자 합치기
n_1 = set() #숫자를 합친 배열 / set을 사용해서 중복 제거 

for i in numbers : #기존 정수 중 범위 안에 있는 값 추가
    if 2 <= i <= 100 :
        n_1.add(i)


for i in range(len(numbers)) : #두 숫자 합치기 
    for j in range(i+1, len(numbers)) : #i 이후의 요소들만 선택
        total = numbers[i] + numbers[j]

        if 2 <= total <= 100 : #  if 활용 범위 필터링
            n_1.add(total)

print(n_1)

