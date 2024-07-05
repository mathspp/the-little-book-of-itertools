class takewhile:
    def __init__(self, predicate, iterable):
        raise NotImplementedError()


def test_takewhile_is_iterator():
    """Verify that `takewhile` is (or, at least, looks like) an iterator."""
    assert hasattr(takewhile, "__next__")
    assert hasattr(takewhile, "__iter__")
    tw = takewhile(bool, [])
    assert iter(tw) is tw


def test_takewhile_is_class():
    """Verify that `takewhile` was defined as a class."""
    assert isinstance(
        takewhile, type
    )  # Check that `takewhile` is defined as a class...
    assert takewhile.__name__ == "takewhile"  # ... with the correct name.


def test_takewhile_empty_iterable():
    """Test `takewhile` with an empty iterable."""
    assert list(takewhile(lambda _: True, [])) == []


def test_takewhile_first_is_false():
    """Test `takewhile` when the first value doesn't satisfy the predicate."""
    assert list(takewhile(lambda _: False, range(15))) == []


def test_takewhile_all_are_true():
    """Test `takewhile` when all of the elements satisfy the predicate."""
    assert list(takewhile(bool, range(2, 15))) == list(range(2, 15))


def test_takewhile():
    """Standard `takewhile` test."""

    def is_even(number):
        return number % 2 == 0

    # We won't reach the evens after the 5   X  v  v  vv
    assert list(takewhile(is_even, [0, 2, 4, 5, 6, 8, 10])) == [0, 2, 4]


def test_takewhile_generator_iterator():
    """Test `takewhile` with a generic iterator as the iterable."""

    def is_even(number):
        return number % 2 == 0

    _values = [0, 2, 4, 5, 6, 8, 10]
    values = (v for v in _values)
    assert list(takewhile(is_even, values)) == [0, 2, 4]
