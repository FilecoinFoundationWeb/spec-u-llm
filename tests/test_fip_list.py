import pytest
from fip_tools.fip_list import get_fip_numbers

def test_get_fip_numbers():
    numbers = get_fip_numbers()
    assert isinstance(numbers, list)
    assert all(isinstance(n, int) for n in numbers)
    assert numbers == sorted(numbers)
    assert all(n >= 0 for n in numbers)
