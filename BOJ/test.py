import sys
import math
from collections import Counter


n = [8,3,1,-2,2,2]

cnt = Counter(n).most_common(2)
print(cnt)

# cnt = Counter(n).most_common(2)
# print(cnt[1][0])