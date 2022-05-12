board = []
# 중복 열 확인
col = [False] * 8
# 오른쪽 대각선 공격 가능 확인
digo_r = [False] * 15
# 왼쪽 대각선 공격 가능 확인
digo_l = [False] * 15
 
 
for _ in range(8):
    row = input()
    board.append(row.strip())
 
res = 0
def queens(r):
    global board, res
    if r == 8:
        res += 1
        return
 
    for i in range(8):
        # 이전 Queen이 놓여져 채워진 col, digo_r, digo_l 에 False라면 queen을 놓는다.
        if board[r][i] != '*' and not col[i] and not digo_r[r + i] and not digo_l[i - r + 7]:
            col[i] = digo_r[r + i] = digo_l[i - r + 7] = True
            queens(r + 1)
            col[i] = digo_r[r + i] = digo_l[i - r + 7] = False
 
queens(0)
print(f'{res}')