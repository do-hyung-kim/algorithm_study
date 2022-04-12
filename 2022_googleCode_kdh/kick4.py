tc = int(input())
for i in range(1, tc+1):
    print(f'Case #{i}: ',end='')
    num = input()
    funs = list(map(int, input().split(' ')))
    funs = [0] + funs
    nodes = list(map(int, input().split(' ')))
    nodes = [0] + nodes
    prev_least = [0 for _ in range(len(nodes))]
    prev_select_idx = [0 for _ in range(len(nodes))]
    dp = [0 for _ in range(len(nodes))]
    res = 0
    for idx in reversed(range(1, len(nodes))):
        pointIdx = nodes[idx]
        prev_idx = prev_select_idx[idx]
        if funs[prev_idx] > funs[idx]:
            funs[idx] = funs[prev_idx]
        if dp[idx] == 0:
            if prev_idx == 0:
                dp[idx] = funs[idx]
            else :
                dp[idx] = dp[prev_idx] + (funs[idx] - funs[prev_idx])
        else :
            dp[idx] += funs[idx] - funs[prev_idx] + dp[prev_idx]

        if pointIdx == 0:
            res += dp[idx]
            continue
        if prev_least[pointIdx] == 0:
            prev_least[pointIdx] = funs[idx]
            prev_select_idx[pointIdx] = idx
        elif prev_least[pointIdx] > funs[idx] :
            dp[pointIdx] += dp[prev_select_idx[pointIdx]]
            prev_least[pointIdx] = funs[idx]
            prev_select_idx[pointIdx] = idx
        else :
            dp[pointIdx] += dp[idx]

    print(res)