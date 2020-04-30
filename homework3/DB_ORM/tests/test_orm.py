
import pytest

from models.models import Human
from orm_client.orm_client import SqlOrmConnection
from tests.orm_builder import SqlOrmBuilder


class TestOrmMysql:

    @pytest.fixture(scope='function', autouse=True)
    def setup(self, orm_client):
        self.mysql: SqlOrmConnection = orm_client
        self.builder = SqlOrmBuilder(orm_client)

    def test_add_data(self):
        data = []
        for _ in range(10):
            data.append(self.builder.add_human())

        j = 0
        for i in self.mysql.session.query(Human).all():
            assert i == data[j]
            j += 1

    def test_delete_data(self):
        for _ in range(10):
            self.builder.add_human()

        self.mysql.session.query(Human).delete()
        assert not len(self.mysql.session.query(Human).all())
        self.mysql.session.commit()



