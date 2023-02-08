import const as c
from const import c
from const import *

if True:
    x
elif False:
    x
else:
    x

while x < y:
    pass

for x in y:
    print(x)

try:
    x
except Exception as ex:
    y
else:
    t
finally:
    z

class x(y):
    def __init__(self, i : int) -> None:
        print(i)
        super().__init__()
    
    @classmethod
    def main (cls):
        pass

def gen():
    yield x

with x as f:
    pass