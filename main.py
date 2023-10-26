import sqlalchemy
from sqlalchemy.orm import sessionmaker
from functions import find_publisher_sales, drop_tables, create_table

DSN = 'postgresql://postgres:mivida1@localhost:5432/orm'
engine = sqlalchemy.create_engine(DSN)

Session = sessionmaker(bind=engine)
session = Session()


if __name__ == "__main__":
    drop_tables(engine)
    create_table(engine)
    find_publisher_sales(session)

session.commit()
session.close()
