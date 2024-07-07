from itertools import count

import pytest


class n_wise:
    def __init__(self, iterable, n):
        raise NotImplementedError()


def test_n_wise_is_iterator():
    """Verify that `n_wise` is (or, at least, looks like) an iterator."""
    assert hasattr(n_wise, "__next__")
    assert hasattr(n_wise, "__iter__")
    nw = n_wise([], 5)
    assert iter(nw) is nw


def test_n_wise_is_class():
    """Verify that `n_wise` was defined as a class."""
    assert isinstance(n_wise, type)  # Check that `n_wise` is defined as a class...
    assert n_wise.__name__ == "n_wise"  # ... with the correct name.


@pytest.mark.parametrize(
    ["n"],
    [
        (1,),
        (2,),
        (3,),
        (42,),
        (73,),
    ],
)
def test_empty_iterable(n):
    """Test `n_wise` with an empty iterable."""
    assert list(n_wise([], n)) == []


@pytest.mark.parametrize(
    ["n"],
    [
        (2,),
        (3,),
        (42,),
        (73,),
    ],
)
def test_short_iterable(n):
    """Test `n_wise` with an iterable that isn't long enough."""
    assert list(n_wise(range(n - 1), n)) == []


@pytest.mark.parametrize(
    ["n"],
    [
        (1,),
        (2,),
        (3,),
        (42,),
        (73,),
    ],
)
def test_big_enough_pairwise(n):
    """Test `n_wise` with an iterable that is long enough for a single value."""
    assert list(n_wise(range(n), n)) == [tuple(range(n))]


def test_n_wise():
    """Test `n_wise` in a regular setting."""
    squares = (x**2 for x in range(7))
    assert list(n_wise(squares, 4)) == [
        (0, 1, 4, 9),
        (1, 4, 9, 16),
        (4, 9, 16, 25),
        (9, 16, 25, 36),
    ]


def test_n_wise_infinite_iterable():
    """Test `n_wise` with an infinite iterable."""
    nw = n_wise(count(), 4)
    for lower, value in zip(range(150), nw):
        assert (lower, lower + 1, lower + 2, lower + 3) == value
