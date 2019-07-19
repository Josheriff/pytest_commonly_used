import pytest

from core.simple.simple import just_a_sum

def test_just_a_sum():
    first_num = 2
    second_num = 3
    
    sum = just_a_sum(first_num,second_num)
    
    assert sum == 5