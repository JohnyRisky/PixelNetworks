import re

from one import *
from two import B


def test():
    a = A()
    b = B()
    assert a.a == 'Result True' # getter property
    assert b.a == 'Result False'
    assert isinstance(a, A)
    assert isinstance(b, B)
    assert isinstance(a, Base) # классы A и В должны наследоваться от Base
    assert isinstance(b, Base)

    try:
        assert a.func()
    except AttributeError:
        pass

    a.a = 9 # сеттер проперти
    assert a.value() == 9 # можно реалиховать метод value в классе Base
    assert a.func() == 9 * 3 * 5
    assert a.func(7) == 7 * 7 * 3

    b.a = 8 # сеттер проперти
    assert b.value() == 8 

    try:
        a.a = 'one'
    except Error as e:
        assert str(e) == 'error one'

    try:
        a.a = None
    except UndefinedError as e:
        assert str(e) == 'None prohibited' # __str__ в UndefinedError
        assert e.message() == 'error message' # метод message с match case
        assert e.message(1) == 'error message one'
        assert e.message(2) == 'error message two'

    assert isinstance(b.func('123-abc-ABC'), re.Match)
    assert b.func('123-abc-ABC').group(1) == '123-abc-ABC'
    assert b.func('  123-abc-ABC').group(1) == '123-abc-ABC'
    assert b.func('123-abc-ABC  ').group(1) == '123-abc-ABC'
    assert b.func(' 123-abce-ABC ').group(1) == '123-abce-ABC'
    assert b.func(' 123-abcef-ABC ').group(1) == '123-abcef-ABC'
    assert b.func('12a-abc-ABC') is None
    assert b.func('123-Abc-ABC') is None
    assert b.func('123-abc-aBC') is None
    assert b.func('12-abc-ABC') is None
    assert b.func('1233-abc-ABC') is None
    assert b.func('123-ab-ABC') is None
    assert b.func('123-abcefe-ABC') is None
    assert b.func('123-abc-AB') is None
    assert b.func('123-abc-ABCC') is None


if __name__ == '__main__':
    test()
    print('done')