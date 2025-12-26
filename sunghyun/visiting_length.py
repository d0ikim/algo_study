# 방문 길이
# https://school.programmers.co.kr/learn/courses/30/lessons/49994

def solution(dirs):
    visited = set()
    # 파이썬 스러운 변수 활용 나쁘지 않음
    x, y = 0, 0
    
    # U: 위쪽(y+1), D: 아래쪽(y-1), R: 오른쪽(x+1), L: 왼쪽(x-1)
    # 좌표평면: x는 좌우, y는 상하
    # 기억이 나지 않아서 초반에는 if 문으로 했음
    moves = {'U': (0, 1), 'D': (0, -1), 'R': (1, 0), 'L': (-1, 0)}
    
    for d in dirs:
        # 이동 좌표
        dx, dy = moves[d]
        # 다음 좌표
        nx, ny = x + dx, y + dy
        
        # 경계 체크 (-5 ~ 5)
        if -5 <= nx <= 5 and -5 <= ny <= 5:
            # 길은 양방향으로 저장 (A->B 와 B->A 는 같은 길)
            visited.add((x, y, nx, ny))
            visited.add((nx, ny, x, y))
            # 위치 이동
            x, y = nx, ny
            
    # 중복 제거
    return len(visited) // 2

# 예시
# "ULURRDLLU" -> 7
# "LULLLLLLU" -> 7

if __name__ == "__main__":
    print(solution("ULURRDLLU")) # 7
    print(solution("LULLLLLLU")) # 7

