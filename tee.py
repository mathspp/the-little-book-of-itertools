from itertools import count


def tee(iterable, n=2):
    raise NotImplementedError()


def test_tee_zero_iterators():
    """Test that `tee` works with `n=2`."""
    assert tuple() == tee([], 0)


def test_tee_one_iterator():
    """Test that `tee` works with `n=1`."""
    returned = tee([], 1)
    assert isinstance(returned, tuple)
    assert len(returned) == 1
    iterator = returned[0]
    assert hasattr(iterator, "__next__")
    assert hasattr(iterator, "__iter__")
    assert iter(iterator) is iterator


def test_tee_basic():
    """Basic test of the `tee` functionality."""
    squares = (x**2 for x in range(10))
    expected = [x**2 for x in range(10)]
    it1, it2 = tee(squares)
    assert list(it1) == expected
    assert list(it2) == expected


def test_tee_basic_interweaved():
    """Basic test of the `tee` functionality."""
    squares = (x**2 for x in range(10))
    it1, it2 = tee(squares)

    assert next(it1) == 0
    assert next(it1) == 1
    assert next(it1) == 4
    assert next(it1) == 9
    assert next(it1) == 16

    assert next(it2) == 0
    assert next(it2) == 1
    assert next(it2) == 4

    assert next(it1) == 25
    assert next(it1) == 36
    assert next(it1) == 49
    assert next(it1) == 64
    assert next(it1) == 81

    assert next(it2) == 9
    assert next(it2) == 16
    assert next(it2) == 25
    assert next(it2) == 36
    assert next(it2) == 49
    assert next(it2) == 64
    assert next(it2) == 81


def test_tee_many_iterators():
    """Test `tee` with `n` set to a “large” value."""
    iterators = tee(range(10), 100)
    for value in range(10):
        for iterator in iterators:
            assert next(iterator) == value


def test_tee_infinite_iterator():
    """Test `tee` with an infinite iterator."""
    it1, it2 = tee(count(), 2)
    for expected, value in zip(range(100), it1):
        assert expected == value
    for expected, value in zip(range(150), it2):
        assert expected == value
