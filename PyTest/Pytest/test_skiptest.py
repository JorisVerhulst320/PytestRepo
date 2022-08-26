import pytest

@pytest.mark.skip
def test_demo_1(reason = "not included in this build"):
    assert True
    
def test_demo_2():
    assert True
    
    