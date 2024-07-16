from itertools import count, islice


class zip_longest:
    def __init__(self, *iterables, fillvalue=None):
        raise NotImplementedError()


def test_zip_longest_is_iterator():
    """Verify that `zip_longest` is (or, at least, looks like) an iterator."""
    assert hasattr(zip_longest, "__next__")
    assert hasattr(zip_longest, "__iter__")
    zl = zip_longest()
    assert iter(zl) is zl


def test_zip_longest_is_class():
    """Verify that `zip_longest` was defined as a class."""
    assert isinstance(
        zip_longest, type
    )  # Check that `zip_longest` is defined as a class...
    assert zip_longest.__name__ == "zip_longest"  # ... with the correct name.


def test_zip_longest():
    """Basic test for `zip_longest`."""
    assert list(
        zip_longest(
            "ab",
            range(4),
        )
    ) == [("a", 0), ("b", 1), (None, 2), (None, 3)]


def test_zip_longest_fillvalue():
    """Basic test for `zip_longest` with a non-default fill value."""
    assert list(
        zip_longest(
            "ab",
            range(4),
            fillvalue="x",
        )
    ) == [("a", 0), ("b", 1), ("x", 2), ("x", 3)]


def test_zip_longest_no_iterables():
    """Test `zip_longest` with no iterables."""
    assert list(zip_longest()) == []
    assert list(zip_longest(fillvalue=3)) == []


def test_zip_longest_single_iterable():
    """Test `zip_longest` with a single iterable."""
    assert list(zip_longest(range(5))) == list(map(lambda x: (x,), range(5)))


def test_zip_longest_single_iterable_fillvalue():
    """Test `zip_longest` with a single iterable."""
    assert list(zip_longest(range(5), fillvalue="x")) == list(
        map(lambda x: (x,), range(5))
    )


def test_zip_longest_single_infinite_iterable():
    """Test `zip_longest` with a single infinite iterable."""
    assert list(islice(zip_longest(count()), 10)) == list(
        map(lambda x: (x,), range(10))
    )


def test_zip_longest_single_iterable_fillvalue():
    assert list(islice(zip_longest(count(), fillvalue="x"), 10)) == list(
        map(lambda x: (x,), range(10))
    )


def test_zip_longest_many_iterables():
    """Test `zip_longest` on many iterables."""
    it1 = []
    it2 = range(3)
    it3 = "ab"
    it4 = "wxyz"
    it5 = range(3)
    assert list(zip_longest(it1, it2, it3, it4, it5)) == [
        (None, 0, "a", "w", 0),
        (None, 1, "b", "x", 1),
        (None, 2, None, "y", 2),
        (None, None, None, "z", None),
    ]


def test_zip_longest_many_iterables_fillvalue():
    """Test `zip_longest` on many iterables."""
    it1 = []
    it2 = range(3)
    it3 = "ab"
    it4 = "wxyz"
    it5 = range(3)
    assert list(zip_longest(it1, it2, it3, it4, it5, fillvalue=True)) == [
        (True, 0, "a", "w", 0),
        (True, 1, "b", "x", 1),
        (True, 2, True, "y", 2),
        (True, True, True, "z", True),
    ]
