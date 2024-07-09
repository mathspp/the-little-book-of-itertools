from itertools import count as _count, islice, product

import pytest


class count:
    def __init__(self, start=0, step=1):
        raise NotImplementedError()


def test_count_is_not_iterator():
    """Test that `count` is not an iterator."""
    c = count()
    assert iter(c) is not c
    assert iter(c) is not iter(c)


def test_count_no_args():
    """Test `count` with no arguments specified (using the defaults)."""
    pairs = list(islice(zip(count(), _count()), 1000))
    assert len(pairs) == 1000
    for value, real in pairs:
        assert value == real


@pytest.mark.parametrize(
    ["start"],
    [
        (0,),
        (5,),
        (999_999_425,),
        (-1262,),
    ],
)
def test_count_start(start):
    """Test `count` when only the first argument is specified."""
    pairs = list(islice(zip(count(start), _count(start)), 1000))
    assert len(pairs) == 1000
    for value, real in pairs:
        assert value == real


def test_count_non_integer_start():
    """Test `count` when the start is not an integer."""
    pairs = list(islice(zip(count(0.5), _count(0.5)), 10))
    assert len(pairs) == 10
    for value, real in pairs:
        assert value == real


@pytest.mark.parametrize(
    ["start", "step"],
    list(
        product(
            [0, 73, -42],
            [
                0,
                1,
                -1,
                5,
            ],
        )
    ),
)
def test_count_start_and_step(start, step):
    """Test `count` when both arguments are specified."""
    pairs = list(islice(zip(count(start, step), _count(start, step)), 1000))
    assert len(pairs) == 1000
    for value, real in pairs:
        assert value == real


def test_count_non_integer_step():
    """Test `count` when the step is not an integer."""
    pairs = list(islice(zip(count(0, 0.5), _count(0, 0.5)), 10))
    assert len(pairs) == 10
    for value, real in pairs:
        assert value == real


def test_count_both_args_non_integers():
    """Test `count` when both arguments are not integers."""
    pairs = list(islice(zip(count(0.5, 0.25), _count(0.5, 0.25)), 10))
    assert len(pairs) == 10
    for value, real in pairs:
        assert value == real
