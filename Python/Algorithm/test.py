def solution(my_string):
    return ''.join(chr(ord(i)+32) if i.isupper() else chr(ord(i)-32) for i in my_string )


print(solution("cccCCC"))