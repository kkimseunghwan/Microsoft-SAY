def solution(score):
    score = [ (a+b)//2 for a,b in score]
    rank = sorted(list(score), reverse=True)
    
    print(score)
    print(rank)
    
    answer = []
    for i in score:
        answer.append(rank.index(i)+1)
        
    return answer


a = [[80, 70], [70, 80], [30, 50], [90, 100], [100, 90], [100, 100], [10, 30]]
b = [[0,0],[1,1],[1,1],[1,1],[1,1],[1,1]]
print(solution(b))