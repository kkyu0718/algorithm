global visit, answer, maxpercent, percent, wins
from itertools import combinations, product
def solution(dice):
    global visit, answer, maxpercent, percent, wins
    wins = 0
    answer = []
    n = len(dice)
    percent=[[0 for i in range(n//2)] for _ in range(n//2)]
    maxpercent = 0
    visit = [0 for _ in range(n)]
    maxs = 0
    
    choice = list(combinations([i for i in range(n)], n//2))
    for c in choice:
        pro = [i for i in product(range(6), repeat=n//2)]
        me = [dice[i] for i in c]
        other = [dice[i] for i in range(n) if i not in c]
        sum1 = []
        sum2 = []
        for p in pro:
            sum1.append(sum(list(map(lambda x: x[1][x[0]], zip(p, me)))))
            sum2.append(sum(list(map(lambda x: x[1][x[0]], zip(p, other)))))
        sum1.sort()
        sum2.sort()
        # print(sum1, sum2)
        s = 0
        p1 = 0
        p2 = 0
        while p1 < len(sum1):
            while p2 < len(sum2) and sum1[p1] > sum2[p2]:
                p2+= 1
            # print("add = ", p2)
            s += (p2)
            p1 += 1
        if s > maxs:
            maxs = s
            answer = c
    # 오름차순
    # print(percent)
    return list(map(lambda x: x+1, answer))

    