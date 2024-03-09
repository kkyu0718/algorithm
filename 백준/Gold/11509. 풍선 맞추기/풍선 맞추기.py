import heapq
answer=0
n = input()
lst = list(map(int, input().split(" ")))
arrow = [0 for i in range(1000000+1)]
for i in range(len(lst)):
    h = lst[i]

    if arrow[h] > 0:
        arrow[h] -= 1
        arrow[h-1] += 1
    else:
        answer += 1
        arrow[h-1] += 1
print(answer)
