"""List"""
import pytest


@pytest.mark.parametrize("lst, exp", [(['abc', 'def', 'gh'], TypeError),
	                                  ([1, 3, [3, 4]], TypeError),
	                                  ([2, 'kek', 6.4], TypeError)])
def test_1(lst, exp):
    """ Проверка функции суммирования"""
    with pytest.raises(TypeError):
        assert sum(lst) == exp


@pytest.mark.parametrize("lst, exp", [([1, 2, 3, 60], [1, 2, 3, 60]),
                                      (['ab', 'c', 'dfg', 'aaa'], ['aaa', 'ab','c', 'dfg']),
                                      ([2.6, 4.5, 1.4], [1.4, 2.6, 4.5])])
def test_2(lst, exp):
    """ Проверка функции сортировки списков"""
    assert sorted(lst) == exp


class TestList:
    """Тесты для списка"""
    list_test = [1, 3, [3, 4], 2.3, 'kek2']

    def test_3(self):
        """Проверка умножения списков"""
        assert len(self.list_test) == 5

    def test_4(self):
        """Проверка умножения списков"""
        with pytest.raises(TypeError):
            self.list_test *= self.list_test

    def test_5(self):
        """ Проверка эквивалентиности среза и разворота списка"""
        list_test = [1, 3, [3, 4], 2.3]
        lst = list_test[::-1]
        list_test.reverse()
        assert lst == list_test
