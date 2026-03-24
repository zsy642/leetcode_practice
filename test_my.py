import pytest
from answer_face_02_07 import getIntersectionNode
import tool
@pytest.mark.parametrize('listcode,listcode2,expect',[
    ([4,1,8,4,5],[5,0,1,8,4,5],8),
    ([0,9,1,2,4],[3,2,4],2),
    ([2,6,4],[1,5],0),
])

def test_getIntersectionNode(listcode,listcode2,expect):
    n0=tool.list2listnode(listcode)
    n1=tool.list2listnode(listcode2)
    result=getIntersectionNode(n0,n1)
    if not result:
        assert result==expect
    else:
        assert result.val==expect


if __name__ == '__main__':
    pass