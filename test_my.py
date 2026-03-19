import pytest
from answer_27 import removeElement
@pytest.mark.parametrize('nums,val,new_nums,lenght',[
    ([1,1,1,1,1,11,1,1,1,1,11,1,1,1,11,1,2,1],1,[11,11,11,2],4),
    ([1,2,3,3,4,5,6],3,[1,2,4,5,6],5),
    ([],2,[],0)
])

def test_removeElement(nums,val,new_nums,lenght):
    assert removeElement(nums,val)==lenght
    nums=nums[:lenght]
    nums.sort()
    new_nums.sort()
    for i in range (lenght-1):
        assert nums[i]==new_nums[i]

if __name__ == '__main__':
    pass