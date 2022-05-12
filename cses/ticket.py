def findIdx(start, end, total, goal):
    mid = (start + end) // 2
    if total[mid] <= goal and total[mid + 1] > goal:
        return mid
    elif total[mid] <= goal and total[mid + 1] <= goal:
        return findIdx(mid, end, total, goal)
    else :
        return findIdx(start, mid ,total, goal)

h, t = map(int, input().split(' '))
prices = list(map(int, input().split(' ')))
customers = list(map(int, input().split(' ')))

prices.sort()

res = []
for customer in customers:
    if len(prices) == 0:
        print(-1)
    elif customer < prices[0]:
        print(-1)
    elif customer >= prices[-1]:
        print(prices.pop())
    else :
        idx = findIdx(0, len(prices), prices, customer)
        print(prices.pop(idx))