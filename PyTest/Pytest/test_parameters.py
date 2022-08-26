import pytest

def sum(a,b):
    return a +b

@pytest.mark.parametrize("input1,input2,output", [(3,6,8),(6,9,15)])
                      
def test_calc_sum_1(input1,input2,output):
    result = sum(input1,input2)
    assert result == output

