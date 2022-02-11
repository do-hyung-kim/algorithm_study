linked = [
  # clock
  #  0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15     switch
    [1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 0
    [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0, 1, 0, 0, 0, 0], # 1
    [0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 1], # 2
    [1, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], # 3
    [0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 0], # 4
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], # 5
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1], # 6
    [0, 0, 0, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 1], # 7
    [0, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0], # 8
    [0, 0, 0, 1, 1, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0], # 9
]

def check_clock(clock):
  for c in clock:
    if c != 12:
      return False
  return True

def switch_push(clock, switch):
  global linked
  for j in range(len(linked[0])):
    if linked[switch][j] == 1:
      clock[j] = (clock[j] % 12) + 3

def rotate_clock(clock, switch):
  # base case
  if switch >= 10:
    return 0 if check_clock(clock) else float('inf')

  max_cnt = float('inf')
  for i in range(4):
    max_cnt = min(max_cnt, i + rotate_clock(clock, switch + 1))
    switch_push(clock, switch)

  return max_cnt

t = int(input())

while t > 0:
  clock = list(map(int, input().split(' ')))

  print(f'{rotate_clock(clock, 0)}')
  t -= 1