from itertools import combinations as _combinations

import pytest


class combinations:
    def __init__(self, iterable, r):
        raise NotImplementedError()


def test_combinations_is_iterator():
    """Verify that `combinations` is (or, at least, looks like) an iterator."""
    assert hasattr(combinations, "__next__")
    assert hasattr(combinations, "__iter__")
    c = combinations([], 1)
    assert iter(c) is c


def test_combinations_is_class():
    """Verify that `combinations` was defined as a class."""
    assert isinstance(
        combinations, type
    )  # Check that `combinations` is defined as a class...
    assert combinations.__name__ == "combinations"  # ... with the correct name.


@pytest.mark.parametrize(
    ["iterable", "r"],
    [
        (range(5), 1),
        (range(5), 2),
        (range(5), 3),
        (range(5), 4),
        (range(5), 5),
        (range(5), 6),
        ("ABC", 2),
        ("ABC", 3),
        ("ABC", 4),
        ("XAZYPTN", 3),
        ("XAZYPTN", 4),
        ("ABAB", 2),
        ("ABAB", 3),
    ],
)
def test_combinations(iterable, r):
    """Test `combinations`."""
    assert list(combinations(iterable, r)) == list(_combinations(iterable, r))
