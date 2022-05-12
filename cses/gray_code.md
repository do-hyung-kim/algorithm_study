# Gray Code
## 문제 설명
```
Gray code는 길이 n의 모든 2n 비트 문자열 리스트인데, 인접하는 두 문자열은 단 하나의 비트만 달라야 한다.(해밍 거리-Hamming distance가 1임)
주어진 n에 대해 Gray code를 생성하자.
```

## Input
- n

## Output
2n 라인의 Gray code

## Constraints
`1 ≤ n ≤ 16`

## Example
Input:
2

Output:
00
01
11
10

## Study Point
1 비트만 다르게 다음 수를 생성해야 한다. 예제를 확인
XOR과 우측 Shift 연산으로 Gray code를 생성할 수 있다.
```
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
```