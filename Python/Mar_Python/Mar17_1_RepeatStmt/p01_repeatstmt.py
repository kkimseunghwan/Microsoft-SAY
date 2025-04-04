
# 1 2 3 4
for i in range(1,4):
    print(i)

print("-----")

# 1 2 3 4 ... 10
for i in range(1,11):
    print(i)

print("-----")

# 1 3 5 7 9
for i in range(1,10,2):
    print(i)

print("-----")

# 9 7 5 3 1
for i in range(9,0,-2):
    print(i)

print("-----")

# 1 + 2 + 3 + 4 + 5
n = 0
for i in range(1,6):
    n += i
print(n)

print("-----")

# 1 + 3 + 5 + 7 + ... 19 = ?
n = 0
for i in range(1,20,2):
    n += i
print(n)

print("-----")

for i in range(1, 10):
    print("2 X %d = %d" % (i, i << 1))
    

print("-----")

for i in range(2, 10):
    for j in range(1, 10):
        print("%d X %d = %d" % (i, j, i * j))


for i in range(1, 10):
    for j in range(2, 10):
        print("%d X %d = %d" % (j, i, i * j), end='\t')
    print()

print("-----")


for i in range(5):
    for j in range(5):
        print("ㅋ", end='')
    print()


print("-----")


for i in range(5):
    for j in range(i):
        print("ㅋ", end='')
    print()


print("-----")


for i in range(5, 0, -1):
    for j in range(i):
        print("ㅋ", end='')
    print()

print("-----")

for i in range(5):
    for j in range(5):
        if i == j: print("ㅋ", end='')
        else: print("  ", end='')

    print()

print("-----")

for i in range(5):
    for j in range(i):
        print("  ", end='')
    print("ㅋ")

print("-----")

for i in range(5):
    for j in range(i * 2 + 1):
        if i&1: print("ㅎ", end='')
        else: print("ㅋ", end='')
    print()

print("-----")

for i in range(5):
    if i&1: print("ㅎ" * (i*2+1))
    else: print("ㅋ"* (i*2+1))
