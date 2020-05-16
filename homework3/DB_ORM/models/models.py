from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


class Human(Base):
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True, autoincrement=True)

    name = Column(String(50), nullable=False)
    job = Column(String(120), nullable=False)

    def __repr__(self):
        return f"(" \
               f"'{self.id}'," \
               f"'{self.name}'," \
               f"'{self.job}'" \
               f")"
