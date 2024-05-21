import pytest

from .main import local_sum


def test_local_sum():
    total = local_sum(1, 2, 3)

    assert total == 6


def test_local_sum_with_str_arg():
    with pytest.raises(TypeError):
        local_sum(1, 2, '3')
