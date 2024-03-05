def solution(number, k):
    answer = ''
    stk = []
    cnt = 0
    for idx, n in enumerate(number):
        # pop 진행
        while stk and stk[-1] < n:
            stk.pop()
            cnt += 1
            if cnt == k:
                # print("cnt == k")
                stk.append(n)
                idx += 1
                return "".join(stk) + number[idx:]
        stk.append(n)
        
        # print("stk = ", stk)
    return "".join(stk[:(len(number)-k)])