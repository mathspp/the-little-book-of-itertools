from itertools import count


class pairwise:
    def __init__(self, iterable):
        raise NotImplementedError()


def test_pairwise_is_iterator():
    """Verify that `pairwise` is (or, at least, looks like) an iterator."""
    assert hasattr(pairwise, "__next__")
    assert hasattr(pairwise, "__iter__")
    pw = pairwise([])
    assert iter(pw) is pw


def test_pairwise_is_class():
    """Verify that `pairwise` was defined as a class."""
    assert isinstance(pairwise, type)  # Check that `pairwise` is defined as a class...
    assert pairwise.__name__ == "pairwise"  # ... with the correct name.


def test_empty_iterable():
    """Test `pairwise` with an empty iterable."""
    assert list(pairwise([])) == []


def test_one_element_iterable():
    """Test `pairwise` with an iterable with a single element."""
    assert list(pairwise([1])) == []


def test_two_element_iterable():
    """Test `pairwise` works with an iterable of two elements."""
    assert list(pairwise([1, 2])) == [(1, 2)]


def test_pairwise():
    """Test `pairwise` in a general setting."""
    squares = (x**2 for x in range(5))
    assert list(pairwise(squares)) == [
        (0, 1),
        (1, 4),
        (4, 9),
        (9, 16),
    ]


def test_pairwise_infinite_iterable():
    """Test `pairwise` with an infinite iterable."""
    pw = pairwise(count())
    for lower, value in zip(range(150), pw):
        assert (lower, lower + 1) == value
