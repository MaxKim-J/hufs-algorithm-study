# 이미 돌렸던 친구인지 아닌지 확인하는 작업 필요. --> 그래서 checked를 추가했는데- 첫번째 TC 7인데 5나옴.
# 3을 돌리기 전에, 양 옆 판단함. 아래 코드는 elif 위에서 걸리면 아래 안함. --> 그래서 if로 다 바꿨습니다. --> 그래도 안되는 군. 순차 진행이라.
# rotateWheel을 각 if문 말고 마지막에 한 번에 하기로 함. 그리고 회전도 if문 다 하고 나서 해야함.
# 그래도 안되는데 아니 deque 마지막에 '\n' 왜 들어감? 그래서 deque마지막에 [:-1] --> 는 sys.stdin.readline 때문 그냥 input 쓰면 ㄱㅊ

from sys import stdin
from collections import deque
input = stdin.readline

def rotateWheel(num, direction, checked):
    rotates = []
    if num == 1 and wheel1[2] != wheel2[-2] and not checked[2] :
        checked[1] = 1
        rotates.append(2)
    if num == 2 and wheel1[2] != wheel2[-2] and not checked[1]:
        checked[2] = 1
        rotates.append(1)
    if num == 2 and wheel2[2] != wheel3[-2] and not checked[3]:
        checked[2] = 1
        rotates.append(3)
    if num == 3 and wheel2[2] != wheel3[-2] and not checked[2]:
        checked[3] = 1
        rotates.append(2)
    if num == 3 and wheel3[2] != wheel4 [-2] and not checked[4]:
        checked[3] = 1
        rotates.append(4)
    if num == 4 and wheel4[-2] != wheel3[2] and not checked[3]:
        checked[4] = 1
        rotates.append(3)
    globals()['wheel{}'.format(num)].rotate(direction)
    rotates = set(rotates)
    for i in rotates:
        rotateWheel(i, -direction, checked)

for _ in range(1,5):
    globals()['wheel{}'.format(_)] = deque(list(input())[:-1])

K = int(input())
rotation = [tuple(map(int,input().split())) for _ in range(K)]

for a, b in rotation:
    checked = [0,0,0,0,0]
    rotateWheel(a,b, checked)

score1 = 0 if wheel1[0]=='0' else 1
score2 = 0 if wheel2[0]=='0' else 2
score3 = 0 if wheel3[0]=='0' else 4
score4 = 0 if wheel4[0]=='0' else 8

# for i in range(4): result += (2**i) * gears[i+1][0]
# gears[i] 해서 안에 deque 쓰면 됐음.

print(score1+score2+score3+score4)


