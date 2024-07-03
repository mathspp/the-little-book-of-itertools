from itertools import count, cycle as _cycle, islice

import pytest


def cycle(iterable):
    raise NotImplementedError()


@pytest.mark.parametrize(
    ["iterable"],
    [
        ([],),
        (set(),),
        ("",),
        ({},),
    ],
)
def test_cycle_empty_iterable(iterable):
    """Test how cycle behaves if given an empty iterable."""
    with pytest.raises(StopIteration):
        next(cycle(iterable))


def test_cycle_single_element():
    """Test how cycle behaves given an iterable with a single element."""
    VALUE = 15
    c = cycle([VALUE])
    for value in islice(c, 1000):
        assert value == VALUE


def test_cycle_many_elements():
    """Test how cycle behaves given an iterable with multiple elements."""
    VALUES = range(15)
    for value, real in islice(zip(cycle(VALUES), _cycle(VALUES)), 1000):
        assert value == real


def test_cycle_empty_arbitrary_iterator():
    """Test how cycle behaves with a more general empty iterator."""
    VALUES = (value for value in range(0, -5))
    with pytest.raises(StopIteration):
        next(cycle(VALUES))


def test_cycle_arbitrary_iterator():
    """Test how cycle behaves with a more general iterator."""
    MAX = 15
    VALUES = (value for value in range(MAX))
    for idx, value in islice(enumerate(cycle(VALUES)), 1000):
        assert value == (idx % MAX)


def test_cycle_works_with_infinite_iterator():
    """Test that cycle still works when fed an infinite iterator."""
    for idx, value in enumerate(islice(cycle(count()), 1000)):
        assert value == idx
