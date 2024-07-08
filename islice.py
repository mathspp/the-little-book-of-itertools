from itertools import count, islice

import pytest


class islice:
    def __init__(self, iterable, *args):
        parsed_args = slice(*args)
        self.step = parsed_args.step or 1
        self.at = -1
        self.next_id = parsed_args.start or 0
        indices = (
            count()
            if parsed_args.stop is None
            else range(max(parsed_args.stop, parsed_args.start or 0))
        )
        self.iterator = zip(indices, iterable)

    def __iter__(self):
        return self

    def __next__(self):
        while self.at < self.next_id:
            self.at, value = next(self.iterator)

        self.next_id += self.step
        return value


def test_islice_is_iterator():
    """Verify that `islice` is (or, at least, looks like) an iterator."""
    assert hasattr(islice, "__next__")
    assert hasattr(islice, "__iter__")
    nw = islice([], 0)
    assert iter(nw) is nw


def test_islice_is_class():
    """Verify that `islice` was defined as a class."""
    assert isinstance(islice, type)  # Check that `islice` is defined as a class...
    assert islice.__name__ == "islice"  # ... with the correct name.


@pytest.mark.parametrize(
    ["stop"],
    [
        (0,),
        (1,),
        (2,),
        (5,),
        (10,),
        (15,),
    ],
)
def test_islice_only_stop(stop):
    """Verify that `islice` works when only `stop` is specified."""
    squares = (x**2 for x in range(10))
    expected = [x**2 for x in range(min(stop, 10))]
    assert list(islice(squares, stop)) == expected


def test_islice_stop_larger_than_iterable():
    """Test `islice` when the value of `stop` is larger than the iterable."""
    squares = (x**2 for x in range(10))
    expected = [x**2 for x in range(10)]
    assert list(islice(squares, 1073)) == expected


def test_islice_only_stop_infinite_iterable():
    """Test `islice` with a value for `stop` and an infinite iterable."""
    assert list(islice(count(), 10)) == list(range(10))


def test_islice_only_stop_none():
    """Test `islice` with a single argument `None`."""
    assert list(islice(range(10), None)) == list(range(10))


def test_islice_only_stop_none_infinite_iterable():
    """Test `islice` with a single argument `None` and an infinite iterable."""
    iterable = count()
    for expected, value in zip(range(150), islice(iterable, None)):
        assert expected == value


@pytest.mark.parametrize(
    ["start", "stop"],
    [
        (None, None),
        (None, 3),
        (0, 4),
        (1, 7),
        (3, 10),
        (5, 15),
        (7, 4),
        (8, None),
    ],
)
def test_islice_start_stop(start, stop):
    """Test `islice` with values for `start` and `stop`."""
    squares = (x**2 for x in range(10))
    expected_range = range(
        start or 0,
        10 if stop is None or stop > 10 else stop,
    )
    expected = [x**2 for x in expected_range]
    assert list(islice(squares, start, stop)) == expected


@pytest.mark.parametrize(
    ["start", "stop", "step"],
    [
        (None, None, None),
        (None, None, 2),
        (None, None, 3),
        (None, 3, None),
        (None, 3, 2),
        (None, 3, 3),
        (0, 4, 2),
        (0, 4, 3),
        (1, 7, 2),
        (1, 7, 3),
        (3, 10, 2),
        (3, 10, 3),
        (5, 15, 2),
        (5, 15, 3),
        (7, 4, 2),
        (7, 4, 3),
        (8, None, None),
        (8, None, 2),
        (8, None, 3),
    ],
)
def test_islice_start_stop_step(start, stop, step):
    """Test `islice` with values for `start`, `stop`, and `step`."""
    squares = (x**2 for x in range(10))
    expected_range = range(
        start or 0,
        10 if stop is None or stop > 10 else stop,
        1 if step is None else step,
    )
    expected = [x**2 for x in expected_range]
    assert list(islice(squares, start, stop, step)) == expected


@pytest.mark.parametrize(
    ["start", "stop", "step"],
    [
        (None, 3, None),
        (None, 3, 2),
        (None, 3, 3),
        (0, 4, 2),
        (0, 4, 3),
        (1, 7, 2),
        (1, 7, 3),
        (3, 10, 2),
        (3, 10, 3),
        (5, 15, 2),
        (5, 15, 3),
        (7, 4, 2),
        (7, 4, 3),
    ],
)
def test_islice_start_stop_step_infinite_iterable(start, stop, step):
    """Test `islice` with all values and an infinite iterable."""
    expected_range = range(
        start or 0,
        stop,
        1 if step is None else step,
    )
    assert list(islice(count(), start, stop, step)) == list(expected_range)


def test_islice_does_not_advance_too_much():
    """Test `islice` does not advance the iterator past what is needed."""
    squares = (x**2 for x in range(10))
    list(islice(squares, 5))
    assert list(squares) == [25, 36, 49, 64, 81]


def test_islice_advances_at_least_the_value_of_start():
    """Test `islice` advances at least `start` items when `stop < start`."""
    squares = (x**2 for x in range(10))
    list(islice(squares, 3, 1))
    assert next(squares) == 9
