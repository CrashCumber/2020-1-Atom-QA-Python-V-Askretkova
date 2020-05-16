


from faker import Faker

from models.models import Base, Human
from orm_client.orm_client import SqlOrmConnection

fake = Faker(locale='en_US')


class SqlOrmBuilder:

    def __init__(self, connection: SqlOrmConnection):
        self.connection = connection
        self.engine = connection.connection.engine
        self.create_people()

    def create_people(self):
        if not self.engine.dialect.has_table(self.engine, 'people'):
            Base.metadata.tables['people'].create(self.engine)

    def add_human(self):
        human = Human(
            name=fake.name(),
            job=fake.job()
        )
        self.connection.session.add(human)
        self.connection.session.commit()
        return human

