n = int(input())
for _ in range(n):
    elem = input()
    left = 0
    right = len(elem)-1
    cnt = 0
    answer = 0
    while(left <= right):
        le = elem[left]
        re = elem[right]

        if le != re:
            # 왼쪽 삭제
            # print(elem[left+1:right+1]== elem[left+1:right+1][::-1])
            # print(elem[left:right], elem[left:right][::-1])
            if elem[left+1:right+1] == elem[left+1:right+1][::-1]:
                answer = 1
            elif elem[left:right] == elem[left:right][::-1]:
                answer = 1
            else: answer = 2
            break
        left += 1
        right -= 1
    
    print(answer)