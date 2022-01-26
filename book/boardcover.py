# L 모양의 블록 만들기
#                     r, c
# 1번 타입(그냥 L자): [(0,0), (1, 0), (1,1)]
# 2번 타입(기역 ㄱ): [(0,0), (0, 1), (1,1)]
# 3번 타입(기역 반대): [(0,0), (0, 1), (1,0)]
# 4번 타입(니은 모양): [(0,0), (1, -1), (1,0)]
blocks = [
    [(0,0), (1, 0), (1,1)],
    [(0,0), (0, 1), (1,1)],
    [(0,0), (0, 1), (1,0)],
    [(0,0), (1, -1), (1,0)]
]

# Debugging 용
def print_board(b):
    for item in b:
        print(f'{item}')

def marking(board, r_i, c_i, b, mark):
    res = True
    for p in b:
        r = r_i + p[0]
        c = c_i + p[1]

        if r < 0 or c < 0 or r >= len(board) or c >= len(board[0]):
            res = False
        else:
            board[r][c] += mark
            if board[r][c] > 1:
                res = False
    return res

def fill_board(board):
    r = c = -1
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                r = i
                c = j
                break
        if c != -1:
            break

    if c == -1:
        return 1

    res = 0
    # 4개의 블록 모양을 현재 r,c 좌표 기준으로 적용하여 보드를 채울 수 있는지 확인
    # 각 r,c를 기준으로 보드에 적용되는 칸에 1을 더 해줘서 채운 블록을 표시
    for block in blocks:
        if marking(board, r, c, block, 1):
            res += fill_board(board)
        # backtracking 해당 블록을 r, c 기준에서 제거
        marking(board, r, c, block, -1)
    return res

tc = int(input())

while tc > 0:
    mr, mc = map(int, input().split(' '))
    board = []

    for _ in range(mr):
        board.append(list(input().rstrip()))

    # 비어있는 칸의 총 수가 3의 배수가 안되면
    # 할 필요가 없음
    total_empty = 0
    for i in range(mr):
        for j in range(mc):
            if board[i][j] == '.':
                # board에서 #(벽)은 1, 통로(.)은 0으로 설정
                board[i][j] = 0
                total_empty += 1
            else:
                board[i][j] = 1

    if total_empty % 3 != 0:
        print('0')
    else:
        print(f'{fill_board(board)}')
    tc -= 1