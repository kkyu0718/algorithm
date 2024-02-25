def solution(order):
    answer = []
    n = len(order)
    idx = 0
    stk = []
    for i in range(1, n+1):
        if i != order[idx]: 
            while stk and order[idx] == stk[-1]:
                answer.append(stk.pop())
                idx += 1
            # stk처리
            if i != order[idx]:
                stk.append(i)
            else:
                answer.append(i)
                idx+= 1
        else:
            answer.append(i)
            idx += 1
        # print(answer)
    # stk 처리
    while stk and order[idx] == stk[-1]:
        answer.append(stk.pop())
        idx += 1
    return len(answer)