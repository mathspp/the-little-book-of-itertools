from itertools import count, islice


class chain:
    def __init__(self, *iterables):
        raise NotImplementedError()


def test_chain_is_iterator():
    """Verify that `chain` is (or, at least, looks like) an iterator."""
    assert hasattr(chain, "__next__")
    assert hasattr(chain, "__iter__")
    p = chain([])
    assert iter(p) is p


def test_chain_from_iterable_is_iterator():
    """Verify that `chain.from_iterable` is (or, at least, looks like) an iterator."""
    cfi = chain.from_iterable([])
    assert hasattr(cfi, "__next__")
    assert hasattr(cfi, "__iter__")
    assert iter(cfi) is cfi


def test_chain_is_class():
    """Verify that `chain` was defined as a class."""
    assert isinstance(chain, type)  # Check that `chain` is defined as a class...
    assert chain.__name__ == "chain"  # ... with the correct name.


def test_chain():
    """Test chain."""
    assert list(chain("ABC", range(3))) == ["A", "B", "C", 0, 1, 2]


def test_chain_empty_iterables():
    """Test chain."""
    assert list(chain("ABC", [], range(3), [])) == ["A", "B", "C", 0, 1, 2]


def test_chain_infinite_iterables():
    """Test chain."""
    list(islice(chain("ABC", count(), "ABC"), 150)) == list("ABC") + list(range(147))


def test_chain_from_iterable():
    """Test chain_from_iterable."""
    iterable = ["ABC", range(3)]
    assert list(chain.from_iterable(iterable)) == ["A", "B", "C", 0, 1, 2]


def test_chain_from_iterable_empty_iterables():
    """Test chain_from_iterable."""
    iterable = ["ABC", [], range(3), []]
    assert list(chain.from_iterable(iterable)) == ["A", "B", "C", 0, 1, 2]


def test_chain_from_iterable_infinite_iterables():
    """Test chain_from_iterable."""
    iterable = ["ABC", count(), "ABC"]
    list(islice(chain.from_iterable(iterable), 150)) == list("ABC") + list(range(147))
