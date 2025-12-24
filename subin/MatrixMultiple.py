def solution(arr1, arr2):
    #1) 두 행렬을 합친 결과행렬 만들기 : 결과값의 행과 열의 개수 만큼 크기 제작
    answer = []

    for i in range(len(arr1)):
        row = []
        for j in range(len(arr2[0])):
            row.append(0)
        answer.append(row)
   
    #2) 두 행렬의 곱한 값을 넣기
    for i in range(len(arr1)) :
        for j in range(len(arr2[0])) :
            num = 0
            for k in range(len(arr1[0])) :
                num = num + (arr1[i][k]*arr2[k][j])
            answer[i][j] = num
            
            
    return answer
