n = int(input())
lst = list(map(int, input().split()))
# n = 5
# lst = [1,3,1,3,1]
# print(filter(lambda x: x == 1, lst))
onecnt = sum(list(map(lambda x: x // 2, lst)))
if sum(lst) % 3 == 0 and onecnt >= sum(lst) // 3:
    print("YES")
else:
    print("NO")