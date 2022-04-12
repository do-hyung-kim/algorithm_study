tc = int(input())
for _ in range(tc):
    tri = int(input())
    dp = [[0 for _ in range(tri)] for _ in range(tri)]
    maxV = 0
    values = []
    for _ in range(tri):
        values.append(list(map(int, input().split(' '))))
    for i in range(len(values)):
        for j in range(len(values[i])):
            # 맨위에 있을 경우 자기 자신이 최대 값
            if i == 0:
                dp[i][j] = values[i][j]
            # 가장 왼쪽에 있는 경우 내려올 수 있는 경우의 수는 1가지
            elif j == 0:
                dp[i][j] = values[i][j] + dp[i-1][j]
            # 이외의 경우는 자기 자신의 최대값이 나올 수 있는 경우가 2가지 뿐
            # prev1 prev2
            #       target
            # prev1 + targetV or prev2 + targetV
            else :
                dp[i][j] = max(values[i][j] + dp[i-1][j], values[i][j] + dp[i-1][j-1])
    for i in range(tri):
        maxV = max(maxV, dp[tri-1][i])
    print(maxV)

         
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