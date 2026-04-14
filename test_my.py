import pytest
from answer_18 import fourSum
import tool
@pytest.mark.parametrize('nums,target,expect',[
    ([1,0,-1,0,-2,2],0,[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]),
    ([2,2,2,2,2],8,[[2,2,2,2]]),
    ([0,0,0,0,0,0,0],1,[]),
    ([0,0,0,0,0,0,0],0,[[0,0,0,0]]),
    ([1,0,0,0,0,0,0,0,1],1,[[0,0,0,1]]),
    ([1,-2,-5,-4,-3,3,3,5],-11,[[-5,-4,-3,1]]),
])

def test_threeSum (nums,target,expect):
    res=fourSum(nums,target)
    assert res==expect



