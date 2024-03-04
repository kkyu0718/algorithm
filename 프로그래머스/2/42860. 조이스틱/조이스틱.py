import re
def solution(name):
    mid = chr(ord("A")+13)

    transforms = sum(list(map(lambda x: ord(x) - ord('A') if ord(x) < ord(mid) else ord("Z")+1-ord(x), list(name))))

    answer = transforms + len(name)-1
    result = re.finditer("A+", name)
    for r in result:
        left = r.start()
        right = len(name)-1-(r.end()-1)
        if left == 0:
            answer = min(answer, right+transforms)
            continue
        if right == 0:
            left -= 1
            while(name[left] == "A"):
                left -= 1
            answer = min(answer, left+transforms)
            continue
        result1 = (left-1)*2 + right 
        result2 = (right)*2 + left-1
        # print("left, right = ",left, right)
        # print(result1, result2)
        answer = min(answer, result1+ transforms)
        answer = min(answer, result2 + transforms)
    # for i in range(len(name)-1, -1, -1):
    #     if name[i]=="A"
    # print(ord("Z")-ord("A"))
    # print(ord("J"), ord("N"), ord("A"))
    return answer