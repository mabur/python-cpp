import math
import pytest
import python.algorithms


def _generator(iterable):
    return (x for x in iterable)


@pytest.mark.parametrize("iterable_factory", [list, tuple, set, iter, _generator])
@pytest.mark.parametrize("length", range(10))
def test_len(iterable_factory, length):
    iterable = iterable_factory(range(length))
    assert python.algorithms.len(iterable) == length

@pytest.mark.parametrize("iterable_factory", [list, tuple, set, iter, _generator])
@pytest.mark.parametrize("element", range(10))
def test_count_empty(element, iterable_factory):
    iterable = iterable_factory(range(0))
    assert python.algorithms.count(iterable, element) == 0

@pytest.mark.parametrize("iterable_factory", [list, tuple, set, iter, _generator])
@pytest.mark.parametrize("length", range(1, 10))
def test_count_first(iterable_factory, length):
    iterable = iterable_factory(range(length))
    assert python.algorithms.count(iterable, 0) == 1

@pytest.mark.parametrize("iterable_factory", [list, tuple, set, iter, _generator])
@pytest.mark.parametrize("length", range(10))
def test_count_if_even(iterable_factory, length):
    iterable = iterable_factory(range(length))
    def is_even(x):
        return x % 2 == 0
    assert python.algorithms.count_if(iterable, is_even) == math.ceil(length / 2)

@pytest.mark.parametrize("iterable_factory", [list, tuple, set, iter, _generator])
@pytest.mark.parametrize("length", range(10))
def test_count_if_odd(iterable_factory, length):
    iterable = iterable_factory(range(length))
    def is_odd(x):
        return x % 2 != 0
    assert python.algorithms.count_if(iterable, is_odd) == math.floor(length / 2)
