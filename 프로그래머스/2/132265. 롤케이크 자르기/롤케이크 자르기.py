def solution(topping):
    answer = 0
    d = {}
    for t in topping:
        if t not in d:
            d[t] = 0
        d[t] += 1
        
    cnt = set()
    for t in topping:
        cnt.add(t)
        d[t] -= 1
        if d[t] == 0:
            d.pop(t)
        if len(cnt) == len(d):
            answer += 1
        # print(cnt, d)
    return answer