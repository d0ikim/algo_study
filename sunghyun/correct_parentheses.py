# 올바른 괄호
# https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    # 스택 수 초기화
    stack_num = 0

    # 문자열 개수 만큼 반복
    for i in s:
        if i == "(":
            # 처음에는 무조건 ( 시작이기 때문에 ( 시작
            stack_num += 1
        # 아닐 경우에 스택에서 pop 하는 느낌으로 -1 한다
        else:
            # stack에 아무값도 없는데 )이게 들어 왔을경우 끝내는 느낌으로 더 이상 할수 없기에 끝낸다
            if stack_num - 1 < 0:
                stack_num = -1
                break
            # stack에 괄호가 쌍으로 맞는게 있다면 pop해서 꺼내는 느낌으로 -1 을 한다
            else:
                stack_num -= 1

    
    return stack_num == 0

# 예시
# "()()"	true
# "(())()"	true
# ")()("	false
# "(()("	false

if __name__ == "__main__":
    print(solution("()()"))     # True
    print(solution("(())()"))   # True
    print(solution(")()("))     # False
    print(solution("(()("))     # False

