n = int(input())
lst = list(map(int, input().split()))

for i in range(1, len(lst)):
    lst[i] += lst[i-1]

# print(lst)
cnt = 0
for i in range(1, len(lst)-1):
    s = lst[-2] - lst[i-1] + lst[i] - lst[0]
    # print("mid =", s)
    cnt = max(cnt, s)

# 벌통 왼쪽
for i in range(1, len(lst)-1):
    s = 0
    s += lst[-1] - (lst[i]-lst[i-1]) - (lst[-1]-lst[-2])
    s += lst[i-1]
    # print("left = ", s)
    cnt = max(cnt, s)

# 벌통 오른쪽
for i in range(1, len(lst)-1):
    s = 0
    s += lst[-1] - (lst[i]-lst[i-1]) - lst[0]
    s += lst[-1] - lst[i]
    # print("right = ", s)
    cnt = max(cnt, s)
print(cnt)