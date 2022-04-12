def checkStore(numStr):
    zigzag = (numStr[0] - numStr[1]) == (numStr[2] - numStr[1])
    diff = numStr[0] - numStr[1]
    prev = numStr[1]
    for idx in range(2, len(numStr)):
        if (prev - numStr[idx]) != diff:
            if not zigzag or (numStr[idx] - prev) != diff:
                return 10
            diff = -1 * diff
        prev = numStr[idx]
            
    if diff == 0:
        return 1
    elif zigzag:
        return 4
    elif diff == 1 or diff == -1:
        return 2
    else:
        return 5


tc = int(input())
for _ in range(tc):
    numStr = list(input())
    numStr = [int(x) for x in numStr]
    dp = [0 for _ in range(len(numStr))]
    dp[2] = checkStore(numStr[0:3])
    dp[3] = checkStore(numStr[0:4])
    dp[4] = checkStore(numStr[0:5])
    for i in range(5,len(dp)):
        dp[i] = min(dp[i-3] + checkStore(numStr[i-2:i+1]), dp[i-4] + checkStore(numStr[i-3:i+1]), dp[i-5] + checkStore(numStr[i-4:i+1]))
    print(dp[-1])