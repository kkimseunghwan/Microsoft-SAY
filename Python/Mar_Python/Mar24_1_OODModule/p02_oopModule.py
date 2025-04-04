
# 1) impoert 패키지명.모듈명
from operator import imod
import animal.pet

# 패키지명.모듈명.클래스명(...)
d = animal.pet.Dog("만득이")
d.printInfo()

# 2)
# import 패키지명.모듈명 as 별칭

import animal.pet as ap

d = ap.Dog("개득이")
print(d)


# 3) from 패키지명.모듈명 import 가뎌롷거

from Mar24 import Dog
d = Dog("춘식이")
d.printInho



d
