import pytest
from answer_19 import removeNthFromEnd
import tool
@pytest.mark.parametrize('listcode,n,expect',[
    ([1,2,3,4,5],2,[1,2,3,5]),
    ([1],1,[]),
    ([1,2],1,[1]),
    ([1,2,3],3,[2,3]),
])

def test_removeNthFromEnd(listcode,n,expect):
    n0=tool.list2listnode(listcode)
    result=removeNthFromEnd(n0,n)
    assert tool.listnode2list(result)==expect


if __name__ == '__main__':
    pass