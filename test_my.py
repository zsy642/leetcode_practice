import pytest
from answer_704 import search
@pytest.mark.parametrize('a,b,expected',[
                         ([0,1,2,3,4],0,0),
                         ([1,2,3,4,5],5,4),
                         ([1,2,3,4],3,2),
                         ([1,2,3,4],2,1),
                         ([1,2,3,4],20,-1),
])

def test_search(a,b,expected):
    assert search(a,b)==expected


if __name__ == '__main__':
    pass