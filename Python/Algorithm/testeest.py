def solution(a, d, included):
    answer = 0
    for idx, num in enumerate(range(a, a+d*(len(included)-1)+1, d)):
        print(idx, num, included[idx])
        if included[idx]: 
            answer += num
    
    return answer

print(solution(3,4,[True, False, False, True, True]))

a + d*(len(included)-1) + 1