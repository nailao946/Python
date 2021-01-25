def test(a):
    if a == 0:
        return 0
    return a + test(a - 1)