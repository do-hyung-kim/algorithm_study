def shortestPath(visited, currentW, cur):
    global n, w
    isArrive = True
    res = float('inf')
    for f in visited:
        if not f:
            isArrive = False
            break
    if isArrive:
        return currentW + w[cur][0]
    
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        temp = shortestPath(visited, currentW + w[cur][i], i)
        res = min(res, temp)
        visited[i] = False
    return res

tc = int(input())
for _ in range(tc):
    n = int(input())
    w = [[0 for _ in range(n)] for _ in range(n)]
    ## DP 시간에 알아보자
    # minw = [[float('inf') for _ in range(n)] for _ in range(n)]
    visited = [False for _ in range(n)]

    for i in range(n):
        weights = input().split('  ')
        for j,v in enumerate(weights):
            if v:
                w[i][j] = float(v)
    print(shortestPath(visited, 0, 0))
