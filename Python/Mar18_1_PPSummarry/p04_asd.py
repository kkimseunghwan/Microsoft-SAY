
# 리스트를 넣어주면 정렬해주는 함수

# 파이썬에 그냥 있긴 함.
# l.sort()

# 정렬 알고리즘 중에 가장 구리고 저질. (실전용X, 연습용)
#   => 버블정렬

####################

# 버블 정렬
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

