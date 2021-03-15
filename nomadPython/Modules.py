# module 전체를 import 할수도 있다
import math

print(math.fabs(-1.2))

# 항상 사용할 것만 import하자
# 특정 module만 import 할때
from math import ceil, fsum

print(ceil(1.2))
print(fsum([1,2,3,4,5,6,7]))

# import의 이름을 바꿔서 사용할 수도 있다
from math import log10 as sexy_log10

print(sexy_log10(100))