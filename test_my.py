import pytest
from answer_977 import sortedSquares
@pytest.mark.parametrize('nums,expect',[
    ([1,2,3,4,5],[1,4,9,16,25]),
    ([0,1,2,3,4,5],[0,1,4,9,16,25]),
    ([-5,-4,-3,-2,-1,0],[0,1,4,9,16,25]),
    ([-5,-4,-3,-2,-1],[1,4,9,16,25]),
    ([-4,-1,0,3,10],[0,1,9,16,100]),
    ([-7,-3,2,3,11],[4,9,9,49,121]),
    ([],[])
])

def test_sortedSquares(nums,expect):
    assert sortedSquares(nums)==expect


if __name__ == '__main__':
    pass