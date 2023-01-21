# test.py


def test_fib():
    """잘 작동하는지 함 보자"""
    assert fib(4) == 3

@profile
def fib(n):
    if n == 1 or n == 2:
        return 1
    return fib(n-1) + fib(n-2)

if __name__ == "__main__":
    fib(4)