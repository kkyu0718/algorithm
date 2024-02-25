def solution(order):
    answer = []
    n = len(order)
    idx = 0
    stk = []
    for i in range(1, n+1):
        stk.append(i)
        while stk and stk[-1] == order[idx]:
            answer.append(stk.pop())
            idx += 1
    return len(answer)