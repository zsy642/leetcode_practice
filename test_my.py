import pytest
from answer_202 import isHappy
import tool
@pytest.mark.parametrize('num,expect',[
    (0,0),
    (1,1),
    (2,0),
    (100,1),
    (19,1),
    (13,1),
    (44,1),
    (81,0),
    (7,1),
    (8,0),
])

def test_isHappy(num,expect):
    res=isHappy(num)
    assert res==expect



