from itertools import permutations as _permutations

import pytest


class permutations:
    def __init__(self, iterable, r=None):
        raise NotImplementedError()


def test_product_is_iterator():
    """Verify that `permutations` is (or, at least, looks like) an iterator."""
    assert hasattr(permutations, "__next__")
    assert hasattr(permutations, "__iter__")
    p = permutations([])
    assert iter(p) is p


def test_product_is_class():
    """Verify that `permutations` was defined as a class."""
    assert isinstance(
        permutations, type
    )  # Check that `permutations` is defined as a class...
    assert permutations.__name__ == "permutations"  # ... with the correct name.


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
        ("XAZYPTN", 3),
        ("XAZYPTN", 4),
        ("ABAB", 2),
        ("ABAB", 3),
    ],
)
def test_permutations(iterable, r):
    """Test permutations."""
    assert list(permutations(iterable, r)) == list(_permutations(iterable, r))


@pytest.mark.parametrize(
    ["iterable"],
    [
        (range(5),),
        ("ABC",),
        ("XAZYPTN",),
        ("ABAB",),
    ],
)
def test_permutations_without_r(iterable):
    """Test `permutations`."""
    assert list(permutations(iterable)) == list(_permutations(iterable))
