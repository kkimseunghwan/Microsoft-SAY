import pandas as pd
import numpy as np

# Python List
a = pd.DataFrame()
a["이름"] = ["홍길동", "이순신", "강감찬"]
a["나이"] = np.array([20, 30, 40])

print(a)
print("-----")

c = [["홍길동", 20],
     ["이순신", 30]]

c = pd.DataFrame(c, columns=["이름", "나이"])
print(c)
print("-----")


# dict + list
d = {"이름": ["홍길동", "이순신", "강감찬"],
     "나이": [20, 30, 40]}
d = pd.DataFrame(d)
print(d)
print("-----"),

# list + dict
e = [ {"이름": "홍길동", "나이": 20},
      {"이름": "이순신", "나이": 30},]
e = pd.DataFrame(e)
print(e)


