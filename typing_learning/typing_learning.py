from typing import Union, Any


def calc_plus(a: int, b: int) -> int:
    return a + b


def calc_minus(a: Union[int, float], b: Any) -> Any:
    return a - b


def to_int(my_list: list[str]) -> list[int]:
    return [int(e) for e in my_list]


if __name__ == '__main__':
    assert calc_plus(2, 3) == 5
    assert calc_plus(-2, -1) == -3
    assert calc_plus(0, 2) == 2
    assert calc_plus(0, -2) == -2
    assert calc_plus(-1, 2) == 1
    assert calc_plus(1, -3) == -2
    assert calc_plus(2, 0) == 2
    assert calc_plus(-2, 0) == -2
    assert calc_plus(-2, 0) == -2
    assert calc_minus(-2, 0) == -2
    assert calc_minus(-2, -2) == 0
    assert calc_minus(2, 2) == 0
    assert calc_minus(2, 4) == -2
    assert calc_minus(4, 2) == 2
    assert to_int(['1', '2', '3']) == [1, 2, 3]
