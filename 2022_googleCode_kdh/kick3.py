tc = int(input())
for i in range(1, tc+1):
    print(f'Case #{i}: ',end='')
    num = input()
    dices = list(map(int, input().split(' ')))
    dices.sort()
    res = 0
    for num in dices:
        if num < (res + 1):
            continue
        res += 1
    print(res)