class dropwhile:
    def __init__(self, predicate, iterable):
        raise NotImplementedError()


def test_dropwhile_is_iterator():
    """Verify that `dropwhile` is (or, at least, looks like) an iterator."""
    assert hasattr(dropwhile, "__next__")
    assert hasattr(dropwhile, "__iter__")
    tw = dropwhile(bool, [])
    assert iter(tw) is tw


def test_dropwhile_is_class():
    """Verify that `dropwhile` was defined as a class."""
    assert isinstance(
        dropwhile, type
    )  # Check that `dropwhile` is defined as a class...
    assert dropwhile.__name__ == "dropwhile"  # ... with the correct name.


def test_dropwhile_is_not_eager():
    """Test that `dropwhile` doesn't drop the first values eagerly."""
    from itertools import count

    evens = count(0, 2)

    def is_even(number):
        return number % 2 == 0

    dropwhile(is_even, evens)  # This should finish.


def test_dropwhile_empty_iterable():
    """Test `dropwhile` with an empty iterable."""
    assert list(dropwhile(lambda _: True, [])) == []


def test_dropwhile_first_is_false():
    """Test `dropwhile` when the first value doesn't satisfy the predicate."""
    assert list(dropwhile(lambda _: False, range(15))) == list(range(15))


def test_dropwhile_empty_result():
    """Test `dropwhile` when all of the values satisfy the preciate."""
    assert list(dropwhile(bool, range(1, 15))) == []


def test_dropwhile():
    """Standard `dropwhile` test."""

    def is_even(number):
        return number % 2 == 0

    # We won't reach the evens after the 5   X  v  v  vv
    assert list(dropwhile(is_even, [0, 2, 4, 5, 6, 8, 10])) == [5, 6, 8, 10]


def test_dropwhile_generator_iterator():
    """Test `dropwhile` with a generic iterator as the iterable."""

    def is_even(number):
        return number % 2 == 0

    _values = [0, 2, 4, 5, 6, 8, 10]
    values = (v for v in _values)
    assert list(dropwhile(is_even, values)) == [5, 6, 8, 10]
