"""String"""
import pytest


@pytest.mark.parametrize("data", [{1, 2},
                                  (1, 2),
                                  1,
                                  1.3])
def test_1(data):
    """Прибавление строки к другим типам данных"""
    with pytest.raises(TypeError):
        data += 'abc'


class TestString:
    """Тесты для строк"""
    @pytest.mark.parametrize("data, exp", [(int('123'), 123),
                                           (list('123'), ['1', '2', '3']),
                                           (set('123'), {'1', '2', '3'})])
    def test_2(self, data, exp):
        """Преобразование строки к другим типам данных"""
        assert data == exp

    @pytest.mark.parametrize("data", ['hello, {}'.format('world'),
                                      '{}, {}'.format('hello', 'world'),
                                      '{1}, {0}'.format('world', 'hello'),
                                      f"{'hello'}, {'world'}",
                                      "%s, %s" % ('hello', 'world')])
    def test_3(self, data):
        """Форматированные строки """
        assert data == 'hello, world'


    @pytest.mark.parametrize("data", ["abc", r'abc'])
    def test_4(self, data):
        """ Эквивалентность кавычек"""
        assert data == 'abc'

    @pytest.mark.parametrize("data", [[1, 2],
                                      {1, 2},
                                      (1, 2),
                                      1.3])
    def test_1(self, data):
        """Умножение строки на другие типы данных"""
        with pytest.raises(TypeError):
            data *= 'abc'
        
