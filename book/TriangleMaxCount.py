tc = int(input())
for _ in range(tc):
    tri = int(input())
    valueDp = [[0 for _ in range(tri)] for _ in range(tri)]
    # 가능한 경로의 수를 저장하는 dp를 따로 생성
    countDp = [[0 for _ in range(tri)] for _ in range(tri)]
    maxV = 0
    res = 0
    values = []
    for _ in range(tri):
        values.append(list(map(int, input().split(' '))))
    for i in range(len(values)):
        for j in range(len(values[i])):
            # 맨위에 있을 경우 자기 자신이 최대 값
            if i == 0:
                valueDp[i][j] = values[i][j]
                # 맨 위에 있을 경우 경로의 수는 1
                countDp[i][j] = 1;
            # 가장 왼쪽에 있는 경우 내려올 수 있는 경우의 수는 1가지
            elif j == 0:
                valueDp[i][j] = values[i][j] + valueDp[i-1][j]
                countDp[i][j] = 1
            # 이외의 경우는 자기 자신의 최대값이 나올 수 있는 경우가 2가지 뿐
            # prev1 prev2
            #       target
            # prev1 + targetV or prev2 + targetV
            else :
                if values[i][j] + valueDp[i-1][j] == values[i][j] + valueDp[i-1][j-1]:
                    valueDp[i][j] = values[i][j] + valueDp[i-1][j]
                    countDp[i][j] = countDp[i-1][j] + countDp[i-1][j-1]
                elif values[i][j] + valueDp[i-1][j] > values[i][j] + valueDp[i-1][j-1]:
                    valueDp[i][j] = values[i][j] + valueDp[i-1][j]
                    countDp[i][j] = countDp[i-1][j]                 
                else :
                    valueDp[i][j] = values[i][j] + valueDp[i-1][j-1]
                    countDp[i][j] = countDp[i-1][j-1]
            if i == len(values) - 1:
                if maxV < valueDp[i][j]:
                    maxV = valueDp[i][j]
                    res = countDp[i][j]
                elif maxV == valueDp[i][j]:
                    res += countDp[i][j]
    print(res)
            
# 6  
# 1  2  
# 3  7  4  
# 9  4  1  7  
# 2  7  5  9  4
# -------------

# 6  0  0  0  0

# 7  8  0  0  0 

# 10 15 12 0  0

# 19 19 16 19 0

# 21 26 24 28 23