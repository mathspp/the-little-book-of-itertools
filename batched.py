class batched:
    def __init__(self, iterable, n):
        raise NotImplementedError()


def test_batched_is_iterator():
    """Verify that `batched` is (or, at least, looks like) an iterator."""
    assert hasattr(batched, "__next__")
    assert hasattr(batched, "__iter__")
    nw = batched([], 5)
    assert iter(nw) is nw


def test_batched_is_class():
    """Verify that `batched` was defined as a class."""
    assert isinstance(batched, type)  # Check that `batched` is defined as a class...
    assert batched.__name__ == "batched"  # ... with the correct name.


def test_batched_mississippi():
    """Verify that `batched` works."""
    assert list(batched("Mississippi", 4)) == [
        ("M", "i", "s", "s"),
        ("i", "s", "s", "i"),
        ("p", "p", "i"),
    ]


def test_batched_even_division():
    """Verify that `batched` works when `n` divides evenly into the source iterable."""
    assert list(batched(range(6), 2)) == [(0, 1), (2, 3), (4, 5)]


def test_batched_too_short():
    """Test `batched` with a short iterable."""
    assert list(batched("abc", 4)) == [("a", "b", "c")]


def test_batched_empty():
    """Test `batched` with an empty iterable."""
    assert list(batched("", 3)) == []


def test_batched_batches_of_one():
    """Test `batched` with `n=1`."""
    assert list(batched("Hello, world!", 1)) == list(
        map(lambda x: (x,), "Hello, world!")
    )
