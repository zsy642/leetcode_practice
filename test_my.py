import pytest
from answer_142 import detectCycle
import tool
@pytest.mark.parametrize('listcode,copy,expect',[
    ([3,2,0,-4],1,1),
])

def test_detectCycle(listcode,copy,expect):
    n0=tool.list2listnode(listcode,copy,1)
    result=detectCycle(n0)
    assert result==expect



if __name__ == '__main__':
    pass