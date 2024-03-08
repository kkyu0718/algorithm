import copy

n = int(input())
before = list(map(int,input()))
after = list(map(int, input()))
cur = copy.deepcopy(before)

cnt = 0

def flip(start, end, s):
    if end >= len(s):
        end = len(s) - 1
    for i in range(start, end+1):
        s[i] = int(not s[i])
    return s

for i in range(1, n):
    if cur[i-1] != after[i-1]:
        cur = flip(i-1, i+1, cur)
        cnt+=1
        # print(cur)

if "".join(map(str, cur)) == "".join(map(str, after)):
    print(cnt)
    exit()

# print("flip first")
cur = copy.deepcopy(before)
cur[0] = int(not cur[0])
cur[1] = int(not cur[1])
cnt = 1
# print(cur)
for i in range(1, n):
    if cur[i-1] != after[i-1]:
        cur = flip(i-1, i+1, cur)
        cnt+=1

if "".join(map(str, cur)) == "".join(map(str, after)):
    print(cnt)
else :
    print(-1)