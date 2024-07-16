from operator import mul
from itertools import count, islice


class accumulate:
    def __init__(self, iterable, function=None, *, initial=None):
        raise NotImplementedError()


def test_accumulate_is_iterator():
    """Verify that `accumulate` is (or, at least, looks like) an iterator."""
    assert hasattr(accumulate, "__next__")
    assert hasattr(accumulate, "__iter__")
    acc = accumulate([])
    assert iter(acc) is acc


def test_accumulate_is_class():
    """Verify that `accumulate` was defined as a class."""
    assert isinstance(
        accumulate, type
    )  # Check that `accumulate` is defined as a class...
    assert accumulate.__name__ == "accumulate"  # ... with the correct name.


def test_accumulate_default():
    """Basic test for `accumulate`."""
    assert list(accumulate([42, 73, 0, 16, 10])) == [42, 115, 115, 131, 141]


def test_accumulate_default_function_and_initial():
    """Basic test for `accumulate` but with a non-default `initial`."""
    assert list(accumulate([42, 73, 0, 16, 10], initial=10)) == [
        10,
        52,
        125,
        125,
        141,
        151,
    ]


def test_accumulate_other_function():
    """Test `accumulate` with a non-default function."""
    from operator import mul

    assert list(accumulate([42, 73, 1, 16, 10], mul)) == [42, 3066, 3066, 49056, 490560]


def test_accumulate_other_function_initial():
    """Test `accumulate` with a non-default function and an `initial` value.."""
    assert list(accumulate([42, 73, 1, 16, 10], mul, initial=0)) == [0, 0, 0, 0, 0, 0]


def test_accumulate_empty():
    """Test `accumulate` with an empty iterable."""
    assert list(accumulate([])) == []


def test_accumulate_infinite_iterable():
    """Test `accumulate` with an infinite iterable."""
    assert (
        list(
            islice(
                accumulate(
                    count(),
                    mul,
                    initial=42,
                ),
                100,
            )
        )
        == [42] + [0] * 99
    )
