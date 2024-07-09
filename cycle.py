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
    values = list(islice(c, 1000))
    assert len(values) == 1000
    for value in values:
        assert value == VALUE


def test_cycle_many_elements():
    """Test how cycle behaves given an iterable with multiple elements."""
    VALUES = range(15)
    pairs = list(islice(zip(cycle(VALUES), _cycle(VALUES)), 1000))
    assert len(pairs) == 1000
    for value, real in pairs:
        assert value == real


def test_cycle_empty_arbitrary_iterator():
    """Test how cycle behaves with a more general empty iterator."""
    VALUES = (value for value in [])
    with pytest.raises(StopIteration):
        next(cycle(VALUES))


def test_cycle_arbitrary_iterator():
    """Test how cycle behaves with a more general iterator."""
    MAX = 15
    VALUES = (value for value in range(MAX))
    pairs = list(islice(enumerate(cycle(VALUES)), 1000))
    assert len(pairs) == 1000
    for idx, value in pairs:
        assert value == (idx % MAX)


def test_cycle_works_with_infinite_iterator():
    """Test that cycle still works when fed an infinite iterator."""
    pairs = list(enumerate(islice(cycle(count()), 1000)))
    assert len(pairs) == 1000
    for idx, value in pairs:
        assert value == idx
