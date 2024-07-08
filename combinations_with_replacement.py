from itertools import combinations_with_replacement as _combinations_with_replacement

import pytest


class combinations_with_replacement:
    def __init__(self, iterable, r):
        raise NotImplementedError()


def test_combinations_with_replacement_is_iterator():
    """Verify that `combinations_with_replacement` is (or, at least, looks like) an iterator."""
    assert hasattr(combinations_with_replacement, "__next__")
    assert hasattr(combinations_with_replacement, "__iter__")
    cwr = combinations_with_replacement([], 2)
    assert iter(cwr) is cwr


def test_combinations_with_replacement_is_class():
    """Verify that `combinations_with_replacement` was defined as a class."""
    assert isinstance(
        combinations_with_replacement, type
    )  # Check that `combinations_with_replacement` is defined as a class...
    assert (
        combinations_with_replacement.__name__ == "combinations_with_replacement"
    )  # ... with the correct name.


@pytest.mark.parametrize(
    ["iterable", "r"],
    [
        (range(5), 1),
        (range(5), 2),
        (range(5), 3),
        (range(5), 4),
        (range(5), 5),
        ("ABC", 2),
        ("ABC", 3),
        ("ABC", 6),
        ("XAZYPTN", 3),
        ("XAZYPTN", 4),
        ("ABAB", 2),
        ("ABAB", 3),
        ("ABAB", 5),
    ],
)
def test_combinations_with_replacement(iterable, r):
    """Test `combinations_with_replacement`."""
    assert list(combinations_with_replacement(iterable, r)) == list(
        _combinations_with_replacement(iterable, r)
    )
