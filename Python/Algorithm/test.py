




def solution(chicken):
    answer = 0
    coupon = chicken
    while coupon//10 >= 1:
        service = coupon//10
        answer += service
        coupon = coupon%10 + service
        service = 0

    return answer

print(solution(1081))