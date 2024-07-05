import pytest


class filterfalse:
    def __init__(self, predicate, iterable):
        raise NotImplementedError()


def test_filterfalse_is_iterator():
    """Verify that `filterfalse` is (or, at least, looks like) an iterator."""
    assert hasattr(filterfalse, "__next__")
    assert hasattr(filterfalse, "__iter__")
    ff = filterfalse(bool, [])
    assert iter(ff) is ff


def test_filterfalse_is_class():
    """Verify that `filterfalse` was defined as a class."""
    assert isinstance(
        filterfalse, type
    )  # Check that `filterfalse` is defined as a class...
    assert filterfalse.__name__ == "filterfalse"  # ... with the correct name.


def test_filterfalse():
    """Simple test for `filterfalse`."""

    def is_big(number):
        return number > 1000

    numbers = [1, 2, 3, 999_999, 723_523_453_245]
    assert list(filterfalse(is_big, numbers)) == [1, 2, 3]


def test_filterfalse_empty_iterable():
    """Test `filterfalse` with an empty iterable."""

    assert list(filterfalse(bool, [])) == []


def test_filterfalse_None_function():
    """Test `filterfalse` with `None` instead of a predicate function."""

    assert list(filterfalse(None, [False, True, 0, 16, [], ()])) == [False, 0, [], ()]
