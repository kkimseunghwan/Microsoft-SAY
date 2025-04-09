
def solution(numbers):
    answer = ''
    return answer


def bubleSort(numbers):
    for i in range(len(numbers)-1, -1, -1):
        for j in range(i):
            if int(numbers[j][0]) < int(numbers[j+1][0]):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers

def bbSort(numbers):
    for i in range(len(numbers)-1, -1, -1):
        for j in range(i):
            if numbers[i]


            if int(numbers[j][0]) < int(numbers[j+1][0]):
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    
    return numbers


numbers = [3, 30, 34, 345, 5, 2, 9, 20, 315, 33]
numbers = [str(x) for x in numbers]

print(bubleSort(numbers))




