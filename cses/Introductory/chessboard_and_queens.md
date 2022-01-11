# Gray Code
## 문제 설명
```
체스보드에 8개의 퀸을 놓도록 하자.
어느 두 퀸도 서로를 공격할 수 있어서는 안된다. 추가적인 도전으로 각 보드에는 비어있거나 이미 예약되어 있을 수 있어서 비어있는 곳만 사용해야 한다.
하지만 예약된 칸은 서로의 공격에서 퀸을 보호할 수 없다.
퀸을 놓을 수 있는 방법은 얼마나 될까?
```

## Input
8줄, 각 라인은 8개의 문자를 가진다. 각 칸이 비어있는 경우(.)이고 예약(*)을 가진다.

## Output
정수 출력: 퀸 8개가 위치할 수 있는 방법의 수

## Example
Input:
........
........
..*.....
........
........
.....**.
...*....
........

Output:
65

## Study Point
- 각 열마다 한개의 Queeen이 놓인다
- 각 퀸은 수직/수평라인에 다른 퀸이 있어서는 안된다
- 각 퀸은 대각선 방향에 다른 퀸이 있어서는 안된다.
- 배열 `col[8]`은 Queen이 놓여진 곳의 해당 열에 다른 퀀을 못 놓게 한다
- 배열 digo_r[15]는 8x8 배열에 각 좌표의 합이 0 ~ 15이고 오른쪽에서 왼쪽 방향으로 내려가는 대각선 중복을 확인한다.
  예를 들어, (1,2)에 queen이 놓이면, 합이 3이 되는 모든 칸에는 queen이 놓일 수 없다.
  (0, 3), (2, 1), (3, 0) 칸은 안됨
- 배열 digo_l[15]는 digo_r에 반대임, 각 좌표의 차이(diff)가 같아서는 안된다. `열의 인덱스 - 행 인덱스 + 7`
  예를 들어, (1,2)는 `2 - 1 + 7`이 되어 같은 공식으로 `8`을 만드는 모든 좌표가 왼쪽에서 오른쪽 방향의 대각선이 된다.
- 각 queen이 놓여지는 자리에서 모든 행/열/대각선에 걸리는지 확인해도 무방할 듯.