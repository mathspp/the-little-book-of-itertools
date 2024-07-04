import pytest


class product:
    def __init__(self, *iterables, repeat=1):
        raise NotImplementedError()


def test_product_is_not_iterator():
    """Test that `product` is not an iterator."""
    p = product(range(4), range(5))
    assert iter(p) is not p
    assert iter(p) is not iter(p)


def test_product_no_iterables():
    """Test `product` with no iterables."""
    assert list(product()) == [()]


def test_product_iterables_no_repeat():
    """Test `product` when `repeat` is set to `0`."""
    assert list(product(range(3), repeat=0)) == [()]
    assert list(product(range(3), range(5), repeat=0)) == [()]


@pytest.mark.parametrize(
    ["iterable"],
    [
        (range(5),),
        ([42, 73, 0, 16, 10],),
        ("abcdefghijk",),
        ("X",),
    ],
)
def test_product_single_iterable(iterable):
    """Test `product` with a single iterable and the default value of `repeat`."""
    assert list(product(iterable)) == [(value,) for value in iterable]


def test_product_single_iterable_repeated():
    """Test `product` with a single iterable and the parameter `repeat`."""
    assert list(product("abc", repeat=3)) == [
        (l1, l2, l3) for l1 in "abc" for l2 in "abc" for l3 in "abc"
    ]


@pytest.mark.parametrize(
    ["outer", "inner"],
    [
        (range(3), "abc"),
        (range(5), range(16)),
        ("itertools", "rocks!"),
    ],
)
def test_product_two_iterables(outer, inner):
    """Test `product` with two iterables."""
    assert list(product(outer, inner)) == [(o, i) for o in outer for i in inner]


def test_product_five_iterables():
    """Test `product` with more than 2 iterables."""
    result = [
        (letter1, num1, boolean, letter2, num2)
        for letter1 in "itertools"
        for num1 in range(5)
        for boolean in [True, False]
        for letter2 in "X"
        for num2 in range(3)
    ]
    assert list(product("itertools", range(5), [True, False], "X", range(3))) == result


def test_product_five_iterables_one_empty():
    """Ensure that `product` works when one of the given iterables is empty."""
    result = [
        (letter1, num1, boolean, letter2, num2)
        for letter1 in "itertools"
        for num1 in range(5)
        for boolean in []
        for letter2 in "X"
        for num2 in range(3)
    ]
    assert list(product("itertools", range(5), [], "X", range(3))) == result


def test_product_five_iterables_repeated():
    """Ensure `product` works with 2+ iterables and the parameter `repeat`."""
    result = [
        (letter1, num1, boolean, letter2, num2, letter3, num3, boolean2, letter4, num4)
        for letter1 in "iter"
        for num1 in range(2)
        for boolean in [True, False]
        for letter2 in "X"
        for num2 in range(3)
        for letter3 in "iter"
        for num3 in range(2)
        for boolean2 in [True, False]
        for letter4 in "X"
        for num4 in range(3)
    ]
    assert (
        list(product("iter", range(2), [True, False], "X", range(3), repeat=2))
        == result
    )
