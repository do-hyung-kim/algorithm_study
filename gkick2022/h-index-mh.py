import heapq

def calculate_hindex(N: int, citations: list):
    minH = []
    ans = []
    hinde = 0
    for i in range(N):
        if citations[i] > hindex:
            heapq.heappush(minH, citations[i])
        # minheap에서 현재 hindex보다 작은 값을 계속 꺼낸다.
        while minH and minH[0] <= hindex:
            heapq.heappop(minH)
        # hindex보다 작은 값을 다 꺼내고 남은 논문의 개수가 hindex보다 크면
        # hindex를 1증가 시킨다.
        if len(minH) >= hindex + 1:
            hindex += 1
        ans.append(hindex)
    return ans
