
def solution(numbers):
    numStr = {
        "zero": '0',
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9'
    }
    answer = ''
    pivot = 0
    while numbers:
        if input():
            print(pivot, numbers[:pivot], "//", numbers, answer)
            if numbers[:pivot] in numStr:
                answer += numStr[numbers[:pivot]]
                numbers = numbers[pivot:]
                pivot = 0
                
            pivot += 1
    
    return answer


a = "onetwothreefourfivesixseveneightnine"
print(solution(a))