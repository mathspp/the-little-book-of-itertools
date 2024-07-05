class compress:
    def __init__(self, data, selectors):
        raise NotImplementedError()


def test_compress_is_iterator():
    """Verify that `compress` is (or, at least, looks like) an iterator."""
    assert hasattr(compress, "__next__")
    assert hasattr(compress, "__iter__")
    c = compress([], [])
    assert iter(c) is c


def test_compress_is_class():
    """Verify that `compress` was defined as a class."""
    assert isinstance(compress, type)  # Check that `compress` is defined as a class...
    assert compress.__name__ == "compress"  # ... with the correct name.


def test_compress_empty_iterables():
    """Test `compress` with two empty iterables."""
    assert list(compress([], [])) == []


def test_compress_boolean_selectors():
    """Test `compress` with Boolean values as selectors."""
    assert list(compress("ABC", [True, False, True])) == ["A", "C"]


def test_compress_non_boolean_selectors():
    """Test `compress` with non-Boolean values as selectors."""
    assert list(compress("ABC", ["yes", "", "also yes"])) == ["A", "C"]


def test_compress_shorter_data():
    """Test `compress` when the data iterable is shorter."""
    assert list(compress("ABCDEFG", [True] * 20)) == list("ABCDEFG")
    assert list(compress("ABCDEFG", [False] * 20)) == []


def test_compress_shorter_selectors():
    """Test `compress` when the selectors iterable is shorter."""
    assert list(compress("ABCDEFG", [True, False])) == ["A"]
