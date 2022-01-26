def findMatch(friend, matched, student):
    first = -1
    for i, v in enumerate(matched):
        if not v:
            first = i
            break
    if first == -1:
        return 1
    res = 0
    for j in range(first, student):
        if not matched[first] and not matched[j] and friend[first][j]:
            matched[first] = True
            matched[j] = True
            res += findMatch(friend, matched, student)
            matched[first] = False
            matched[j] = False
    return res   

TestCase = int(input())
# for 루프와 *로 이차원 리스트를 만들 떄 reference와 value 차이를 확인해보기
# b = [[False] * 11 ] * 11  <---- inner list가 레퍼런스가 된다. 
for _ in range(TestCase):
    c = input().split(' ')
    student = int(c[0])
    pair_num = int(c[1])
    friend = [[False for _ in range(student)] for _ in range(student)]
    matched = [False for _ in range(student)]
    pair = input().split(' ')
    for i in range(pair_num):
        friend[int(pair[2 * i])][int(pair[2 * i + 1])] = True
        friend[int(pair[2 * i + 1])][int(pair[2 * i])] = True
    print(findMatch(friend, matched, student))