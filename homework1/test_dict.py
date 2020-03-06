"""Dict"""
import pytest


@pytest.mark.parametrize("dct, lst",
                         [({1: 'a', 2: 'b', 3: 'c'}, ['a', 'b', 'c']),
                          ({1: [1, 2], 2: [3, 4]}, [[1, 2], [3, 4]])])
def test_1(dct, lst):
    """Проверка значений словаря"""
    assert list(dct.values()) == (lst)


@pytest.mark.parametrize("dct, lst",
                         [({1: 'a', 2: 'b', 3: 'c'}, [1, 2, 3]),
                          ({1: [1, 2], 2: [3, 4]}, [1, 2])])
def test_2(dct, lst):
    """Проверка значений ключей"""
    assert list(dct.keys()) == (lst)


class TestDict:
    """Тесты для словаря"""
    dct_test = {1: 3, 2: 2.3, 3: 'kek2'}

    def test_3(self):
        """Проверка сложения словаря"""
        with pytest.raises(TypeError):
            self.dct_test += self.dct_test

    def test_4(self):
        """Проверка умножения словаря"""
        with pytest.raises(TypeError):
            self.dct_test *= self.dct_test

    def test_5(self):
        """ Проверка обновления ключа словаря"""
        tmp = dict(self.dct_test)
        self.dct_test.update({1: 8})
        assert tmp != self.dct_test
