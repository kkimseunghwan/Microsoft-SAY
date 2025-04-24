def solution(s):
    s = s.split(' ')
    return sum(int(s[i]) if s[i] != 'Z' else -int(s[i-1]) for i in range(len(s)))

print(solution("1 2 Z 3"))

