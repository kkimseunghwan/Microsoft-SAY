
# DTO (Data Transfer Object)
# VO (Value Object)

# [M] : Back-end 개발자

class Company:
    def __init__(self, name, addr, ceo, emp):
        self.name = name
        self.addr = addr
        self.ceo = ceo
        self.emp = int(emp)

    