# 문자열 a와 b 사이의 레벤슈타인 거리
def distance(a, b):
    # 두 문자열이 같으면 거리0 반환
    if a == b:
        return 0
    # 한 쪽만 빈 문자열이면 다른 문자열의 길이를 거리로 반환
    if a == "":
        return len(b)
    if b == "":
        return len(a)
    
    # 문자열a를 세로축, 문자열b를 가로축으로 빈 이중배열 초기화
    matrix =  [[[] for j in range(len(b) + 1)] for i in range(len(a) + 1)]
    # 문자열만큼 숫자 채우기, 이중배열 나머지 칸은 0
    for i in range(len(a) + 1):
        for j in range(len(b) + 1):
            if i == 0:
                matrix[i][j] = j
            elif j == 0:
                matrix[i][j] = i
            else:
                matrix[i][j] = 0
    # 
    for i in range(1, len(a) + 1):
        ac = a[i - 1]
        for j in range(1, len(b) + 1):
            bc = b[j - 1]
            # 동일이면 좌상 숫자 가져오기, 변경이면 좌상 숫자에 1 더하기
            cost = 0 if ac == bc else 1
            # 제거, 삽입, 변경 중 최소 거리
            matrix[i][j] = min(matrix[i - 1][j] + 1, matrix[i][j - 1] + 1, matrix[i - 1][j - 1] + cost)
    # 마지막 수를 레벤슈타인 거리로 출력
    return matrix[len(a)][len(b)]
