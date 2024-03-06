from collections import deque

answer = 0

n = input()
lst = list(map(int, input().split(" ")))
lst.sort()
q = deque(lst)

# print(lst)
while len(q) >= 2:
    small = q.popleft()
    big = q.pop()
    # print(small, big)
    # print(q)
    answer += big * 2

print(answer if len(q) == 0 else answer + q[0])
