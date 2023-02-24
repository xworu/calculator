from main import fn


def test_fn():
    assert fn(1, '+', 1) == 2
    assert fn(78, '+', 3) == 81
    assert fn(38, '-', 39) == -1
    assert fn(11, '-', 7) == 4
    assert fn(3, '*', 0) == 0
    assert fn(7, '*', 3) == 21
    assert fn(56, '/', 7) == 8
    assert fn(57, '/', 1) == 57
