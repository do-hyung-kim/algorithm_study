tc = int(input())
goal = 1000000
for i in range(1, tc+1):
    print(f'Case #{i}: ',end='')
    prints = []
    least = []
    total = 0
    for _ in range(3):
        prints.append(list(map(int, input().split(' '))))
    for j in range(4):
        temp = min(prints[0][j], prints[1][j], prints[2][j])
        least.append(temp)
        total += temp
    if total < goal:
        print('IMPOSSIBLE')
        continue
    elif total == goal:
        for num in least:
            print(num, end = ' ')
        print()
        continue
    res = least
    tok = total - goal
    while(tok != 0):
        for idx in range(4):
            if res[idx] > tok:
                res[idx] -= tok
                tok = 0
            else :
                tok -= res[idx]
                res[idx] = 0
    for num in res:
        print(num, end = ' ')
        print()
