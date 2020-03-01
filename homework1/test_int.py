"""Int"""
import pytest


@pytest.mark.parametrize("data", 
                         [[1, 2],
	                      {1, 2},
	                      (1, 2),
	                      'abc'])
def test_1(data):
    """Прибавление целого числа к другим типам данных"""
    with pytest.raises(TypeError):
        data += 4
        assert False


class TestInt:
    """Тесты для целых чисел"""
    @pytest.mark.parametrize("data, exp",
                             [([1, 2], [1, 2, 1, 2, 1, 2, 1, 2]),
                              ((1, 2), (1, 2, 1, 2, 1, 2, 1, 2)),
                              ('abc', 'abcabcabcabc')])
    def test_2(self, data, exp):
        """Умножение целого числа на другие типы данных"""
        res = 4 * data
        assert res == exp

    @pytest.mark.parametrize("data", [100000, 0, 34])
    def test_3(self, data):
        """ Тип данных при возведение целого числа в степень"""
        assert type(data) == type(pow(data, data))


    @pytest.mark.parametrize("data", [100, 0, -100])
    def test_4(self, data):
        """ Деление на ноль"""
        with pytest.raises(ZeroDivisionError):
            assert data / 0


    @pytest.mark.parametrize("data", [100, 0, -100])
    def test_5(self, data):
        """ Проверка получения целой части от деления целого числа на большее целое число """
        if data + 1000 > 0 and data < 0:
            assert - 1 == (data // (data + 1000))
        else:
            assert 0 == (data // (data + 1000))