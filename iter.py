def iter(function, obj):
    raise NotImplementedError()


def test_iter_immediate():
    """Test that `iter` won't call the function after returning the target value."""

    def immediate():
        return 0
        assert False  # Shouldn't reach here.

    list(iter(immediate, 0))


def test_iter_some_iterations():
    """Test that `iter` generally works fine."""
    counter = 0

    def function():
        nonlocal counter
        counter += 1
        return counter

    assert list(iter(function, 10)) == list(range(1, 10))
