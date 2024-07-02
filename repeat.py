from itertools import islice, product

import pytest


def repeat(object, times=None):
    raise NotImplementedError()


@pytest.mark.parametrize(
    ["obj", "times"],
    list(
        product(
            [True, False, object, object(), "bananas", 15, [], {}],
            [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 113],
        )
    ),
)
def test_repeat_finite(obj, times):
    """Test whether `repeat` respects the number of times something should be repeated."""
    values = list(islice(repeat(obj, times), times + 5))
    assert len(values) == times
    assert all(value is obj for value in values)


def test_repeat_infinite():
    """Test whether `repeat` works when the second argument is not specified.

    This doesn't really test whether `repeat` is infinite or not, but it's an
    approximation.
    """
    repeated = repeat(15)
    for _, value in zip(range(999_999), repeated):
        assert value == 15
