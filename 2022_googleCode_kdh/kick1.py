tc = int(input())
for i in range(1, tc+1):
    print(f'Case #{i}:')
    r, c = map(int, input().split(' '))
    for i in range(r):
        upline = '+-' * c + '+'
        downline = '|.' * c + '|'
        if i == 0:
            upline = '..' + '+-' * (c-1) + '+'
            downline = '..' + '|.' * (c-1) + '|'
        print(upline)
        print(downline)
    print('+-' * c + '+')