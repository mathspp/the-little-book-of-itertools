from itertools import count, islice, repeat


class starmap:
    def __init__(self, function, iterable):
        raise NotImplementedError()


def test_starmap_is_iterator():
    """Verify that `starmap` is (or, at least, looks like) an iterator."""
    assert hasattr(starmap, "__next__")
    assert hasattr(starmap, "__iter__")
    sm = starmap(lambda: None, [])
    assert iter(sm) is sm


def test_starmap_is_class():
    """Verify that `starmap` was defined as a class."""
    assert isinstance(starmap, type)  # Check that `starmap` is defined as a class...
    assert starmap.__name__ == "starmap"  # ... with the correct name.


def test_starmap():
    """Basic test for `starmap`."""
    assert list(
        starmap(
            pow,
            zip(
                [10, 10, 10, 10],
                [2, 3, 4, 5],
            ),
        )
    ) == [100, 1000, 10000, 100000]


def test_starmap_empty_iterable():
    """Test `starmap` with an empty iterable argument."""
    assert list(starmap(pow, [])) == []


def test_starmap_infinite_iterables():
    """Test `starmap` with infinite iterables."""
    assert list(
        islice(
            starmap(
                pow,
                zip(
                    repeat(10),
                    count(),
                ),
            ),
            5,
        )
    ) == [
        1,
        10,
        100,
        1000,
        10000,
    ]


def test_starmap_many_arguments():
    """Test `starmap` with a function that takes more than 2 arguments."""
    assert list(
        starmap(
            max,
            zip(
                [1, 2, 3, 4, 5],
                [2, 3, 4, 5, 1],
                [3, 4, 5, 1, 2],
                [4, 5, 1, 2, 3],
                [5, 1, 2, 3, 4],
            ),
        )
    ) == [5, 5, 5, 5, 5]
