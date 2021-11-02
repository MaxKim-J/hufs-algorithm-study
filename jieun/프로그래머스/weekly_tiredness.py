from itertools import permutations
def solution(k, dungeons):
    answer = -1
    p = list(permutations(dungeons, len(dungeons)))
    for i in p:
        num = 0
        current = k
        for j in range(len(i)):
            if current >= i[j][0]:
                current -= i[j][1]
                num += 1
        if num > answer:
            answer = num
    return answer