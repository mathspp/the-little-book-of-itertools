from itertools import count

import pytest


class groupby:
    def __init__(self, iterable, key=None):
        raise NotImplementedError()


def remainder_by_two(x):
    return x % 2


def test_groupby_is_iterator():
    """Verify that `groupby` is (or, at least, looks like) an iterator."""
    assert hasattr(groupby, "__next__")
    assert hasattr(groupby, "__iter__")
    gb = groupby([])
    assert iter(gb) is gb


def test_groupby_is_class():
    """Verify that `groupby` was defined as a class."""
    assert isinstance(groupby, type)  # Check that `groupby` is defined as a class...
    assert groupby.__name__ == "groupby"  # ... with the correct name.


def test_groupby_basic():
    """Basic test for `groupby`."""
    numbers = [0, 2, 4, 6, 7, 8, 9, 10, 11, 13, 15, 17, 18]
    gb = groupby(numbers, remainder_by_two)
    key, group = next(gb)
    assert key == 0
    assert list(group) == [0, 2, 4, 6]
    key, group = next(gb)
    assert key == 1
    assert list(group) == [7]
    key, group = next(gb)
    assert key == 0
    assert list(group) == [8]
    key, group = next(gb)
    assert key == 1
    assert list(group) == [9]
    key, group = next(gb)
    assert key == 0
    assert list(group) == [10]
    key, group = next(gb)
    assert key == 1
    assert list(group) == [11, 13, 15, 17]
    key, group = next(gb)
    assert key == 0
    assert list(group) == [18]
    with pytest.raises(StopIteration):
        next(gb)


def test_groupby_empty_iterable():
    """Test `groupby` with an empty iterable."""
    gb = groupby([], remainder_by_two)
    assert list(gb) == []


def test_groupby_empty_iterable_no_function():
    """Test `groupby` with an empty iterable and no key function."""
    gb = groupby([])
    assert list(gb) == []


def test_groupby_no_function():
    """Test `groupby` with no key function."""
    values = [True, False, False, True, True]
    gb = groupby(values)
    value, group = next(gb)
    assert value is True
    assert list(group) == [True]
    value, group = next(gb)
    assert value is False
    assert list(group) == [False, False]
    value, group = next(gb)
    assert value is True
    assert list(group) == [True, True]


def test_groupby_returns_iterators_connected_with_original_iterator():
    """Test that the groups returned by `groupby` are iterators that
    share the underlying data with the `groupby` object."""

    numbers = [0, 2, 4, 6, 7, 8, 9, 10, 11, 13, 15, 17, 18]
    gb = groupby(numbers, remainder_by_two)
    results = list(gb)
    assert len(results) == 7
    for _, group in results:
        assert len(list(group)) == 0


def test_groupby_infinite_iterator():
    """Test `groupby` with an infinite iterator."""
    gb = groupby(count(), lambda x: x // 3)
    key, group = next(gb)
    assert key == 0
    assert list(group) == [0, 1, 2]
    next(gb)  # 1
    next(gb)  # 2
    next(gb)  # 3
    key, group = next(gb)
    assert key == 4
    assert list(group) == [12, 13, 14]
    key, group = next(gb)
    assert key == 5
    assert list(group) == [15, 16, 17]
