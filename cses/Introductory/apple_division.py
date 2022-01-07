'''
Input의 리스트 요소 개수가 20개면 Timeout이 남
'''
n = int(input())
nums = list(map(int, input().split(' ')))
 
sum_a = 0
 
total = sum(nums)
min_diff = float('inf')
 
for i in range(0, int(2**n)):
    temp = []
    for j in range(n):
        if i & (1 << j):
            sum_a += nums[j]
    min_diff = min(min_diff, abs((total - sum_a) - sum_a))
    sum_a = 0
 
print(min_diff)