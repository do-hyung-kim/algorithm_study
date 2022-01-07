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