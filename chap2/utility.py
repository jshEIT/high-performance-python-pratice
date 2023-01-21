import time

if 'line_profiler' not in dir() or 'profile' not in dir():
    def profile(func):
        return func


def test_some_fn():
    """Check basic behaviors for our function"""

    assert some_fn(2) == 4
    assert some_fn(1) == 1
    assert some_fn(-1) == 1

@profile
def some_fn(useful_input):
    """An expensive function that we wish to both test and profile"""
    # artificial "We are doing something clever and expensive" delay
    time.sleep(1)
    return useful_input ** 2


if __name__ == "__main__":
    print(f"Example call 'some_fn(2)' == {some_fn(2)}")

