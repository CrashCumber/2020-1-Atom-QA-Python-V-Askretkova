"""Set"""
import pytest


@pytest.mark.parametrize("st, lst", [({1, 2, 3, 4, 5}, [1, 2, 3, 4, 5]),
                                     (set('abc'), list('abc')),
                                     ({2, 3, 4}, [3, 4, 2])])
def test_1(st, lst):
    """Проверка эквивалентиности множеств и списка с одинаковыми элементами"""
    assert st == set(lst)


class TestSet:
    """Тесты для множества"""
    set_test = {1, 3, 2.3, 'kek2'}

    def test_2(self):
        """Проверка сложения множеств"""
        with pytest.raises(TypeError):
            self.set_test += self.set_test

    def test_3(self):
        """Проверка умножения множеств"""
        with pytest.raises(TypeError):
            self.set_test *= self.set_test

    def test_4(self):
        """ Проверка эквивалентиности множеств с одинаковыми элементами"""
        set1 = set('1sdf')
        set2 = set('1sdf')
        assert set1 == set2

    def test_5(self):
        """ Проверка уникальности элемента множества"""
        tmp = self.set_test
        tmp.add(1)
        tmp.add('kek2')
        assert tmp == self.set_test
