import sys

import re

s=sys.stdin. read().split()[0]

s=re.sub(r'\d','number',s)

print(s)