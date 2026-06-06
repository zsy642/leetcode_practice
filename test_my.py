import pytest
from answer_18 import fourSum
import tool
@pytest.mark.parametrize('nums,target,expect',[
    ([1,2,3,4,5,null,7], [1,#,2,3,#,4,5,7,#]),
([], []),
([1,2], [1,#,2,#]),
([1,2,2,null,3,null,3], [1,#,2,2,#,3,3,#]),
([1,2,2,3,4,4,3], [1,#,2,2,#,3,4,4,3,#]),
([1,null,2,3], [1,#,2,#,3,#]),
([1,2,3,4,5,null,8,null,null,6,7,9], [1,#,2,3,#,4,5,8,#,6,7,9,#]),
([4,2,7,1,3,6,9], [4,#,2,7,#,1,3,6,9,#]),
([2,1,3], [2,#,1,3,#]),
([1], [1,#]),
([1,null,3], [1,#,3,#]),
([2,3,3,4,5,null,4], [2,#,3,3,#,4,5,4,#]),
([1,3,null], [1,#,3,#]),

])

def test_threeSum (nums,target,expect):
    res=fourSum(nums,target)
    assert res==expect



