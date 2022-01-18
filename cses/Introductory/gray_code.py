def grey_code(g):
    n = 1 << g
 
    '''
            N                    N>>1                  gray
    0      0000           .        0000           .      0000           .
            | >xor = 0001             >xor = 0000           >xor = 0001
    1      0001          .         0000          .       0001          .
            || >xor = 0011           | >xor = 0001           >xor = 0010
    2      0010           .        0001           .      0011           .
            | >xor = 0001             >xor = 0000           >xor = 0001
    3      0011         .          0001         .        0010         .
            ||| >xor = 0111          || >xor = 0011           >xor = 0100
    4      0100                    0010                  0110
    '''
    for i in range(n):
        x = i ^ (i >> 1)
        yield x
 
num = int(input())
 
for i in grey_code(num):
    print(f'{i:0{num}b}')
    
    
# another Solution
'''
        N = 1
        0
        1
        
        N = 2
        0  (N=1)                0 + 0   00
        1                       0 + 1   01
        -                       -----
        1  (N=1 Reverse)        1 + 1   11
        0                       1 + 0   10
        
        N = 3
        00 (N=2)                0 + 00  000 
        01                      0 + 01  001
        11                      0 + 11  011
        10                      0 + 10  010
        --                      ------
        10 (N=2 Reverse)        1 + 10  110
        11                      1 + 11  111
        01                      1 + 01  101
        00                      1 + 00  100
'''
# a = int(input())
# num = pow(2,a)

# def helper(n):
#     if n == 0:
#         return ['0']
#     if n == 1:
#         return ['0', '1']
#     res = helper(n - 1)
#     return ['0' + s for s in res] + ['1' + s for s in res[::-1]]

# list = helper(a)
# for gray in list:
#     print(gray)
