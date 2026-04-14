import pytest
from answer_15 import threeSum
import tool
@pytest.mark.parametrize('nums,expect',[
    ([-1,0,1,2,-1,-4],[[-1,-1,2],[-1,0,1]]),
    ([0,1,1],[]),
    ([0,0,0],[[0,0,0]]),
    ([-1,-1,2],[[-1,-1,2]]),
    ([1,2,0,1,0,0,0,0],[[0,0,0]]),
    ([-2,1,1],[[-2,1,1]]),
    ([0,0,0,0],[[0,0,0]]),
])

def test_threeSum(nums,expect):
    res=threeSum(nums)
    assert res==expect



