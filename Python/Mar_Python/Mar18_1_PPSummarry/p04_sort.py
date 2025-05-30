
# 리스트를 넣어주면 정렬해주는 함수

# 파이썬에 그냥 있긴 함.
# l.sort()

'''
한국어로
1. 현재 자리하고 다음 자리의 수를 비교해서 뒷자리 수가 더 크면 자리를 바꾸기.
예) 6 3 5 4 1 2
pass1 = 3 5 4 1 2 6
pass2 = 3 4 1 2 5 6
pass3 = 3 1 2 4 5 6
pass4 = 1 2 3 4 5 6
=> 버블
'''

# 정렬 알고리즘 중에 가장 구리고 저질. (실전용X, 연습용)
#   => 버블정렬

####################

# 버블 정렬
from operator import index


def BubbleSort(l):
    list_len = len(l)
    
    for i in range(list_len-1, 0, -1):
        isSwap = False # 교환 발생 체크
        for j in range(i):
            if l[j] > l[j+1]:
                l[j], l[j+1] = l[j+1], l[j]
                isSwap = True
        
        if not isSwap:
            break

####################

l = [ 234, 12, 54, 567, 45, 24, 8 ]
print(l)

BubbleSort(l) # 직접 리스트를 수정함.
print(l)

####################
print("-----")
####################

'''
배열을 훑어보고
제일 작은 값을 찾아서
앞으로 보내고 

그거 뺴고 훑어가지고
제일 작은 값을
그 다음 앞으로 보내고
=> 인간적인? 알고리즘
=> 선택 정렬 (Selection Sort)
'''

# l = [234, 12, 1, 54, 5]
# 0턴) 234, 12, 1, 54, 5 중에 제일 작은걸 찾아서(1) 0번과 자리 교체
# 1턴) 1, 12, 234, 54, 5 중에 제일 작은걸 찾아서(5) 1번과 자리 교체
# 2턴) 1, 5, 234, 54, 12 중에 제일 작은걸 찾아서(12) 2번과 자리 교체
# ...

####################

# 최소값 자리수 반환
def getMinIndex(start, l):
    index = start
    minNum = l[start]
    for i in range(start, len(l)):
        if l[i] < minNum:
            minNum = l[i]
            index = i
    return index

# 선택 정렬
def selection_sort(l):
    for i in range(len(l)):
        min_index = getMinIndex(i, l)
        if i != min_index:
            l[i], l[min_index] = l[min_index], l[i]


# GOAT
def selectionSortGoat(l):
    for i in range(len(l) - 1):
        for j in range(i+1, len(l)):
            if l[i] > l[j]:
                l[i], l[j] = l[j], l[i]

####################

l = [234, 12, 1, 54, 5]
print(l)

selection_sort(l)
print(l)

print("-----")
l = [234, 12, 1, 54, 5]
selectionSortGoat(l)
print(l)
