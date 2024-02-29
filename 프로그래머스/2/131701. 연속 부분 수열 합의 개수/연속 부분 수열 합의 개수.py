def solution(elements):
    answer = 0
    n = len(elements)
    result = set()
    
    for i in range(1, n):
        elements[i] += elements[i-1]
    # print(elements)
    
    for start in range(n):
        for end in range(n):
            if start <= end:
                if start == 0: result.add(elements[end])
                else: result.add(elements[end] - elements[start-1])
            else:
                result.add(elements[end] + elements[-1] - elements[start-1])
    # print(result)
            
    return len(result)