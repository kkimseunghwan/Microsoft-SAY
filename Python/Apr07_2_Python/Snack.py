
# DTO (Data Transfer Object)
# VO (Value Object)

# [M] : Back-end 개발자

from datetime import datetime


class Snack:
    def __init__(self, no, name, exp, price, weight, c_name):
        self.no = no
        self.name = name
        self.exp = exp 
        self.price = int(price)
        self.weight = int(weight)
        self.c_name = c_name

    def SnackInfo(self, c_addr, c_ceo, c_emp):
        self.c_addr = c_addr
        self.c_ceo = c_ceo
        self.c_emp = c_emp
        return self

