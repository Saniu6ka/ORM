from sqlalchemy import text
from sqlalchemy.orm import declarative_base

Base = declarative_base()

def drop_tables(engine):
    with engine.connect() as conn:
        conn.execute(text('DROP TABLE IF EXISTS sale CASCADE'))
        conn.execute(text('DROP TABLE IF EXISTS stock CASCADE'))
        conn.execute(text('DROP TABLE IF EXISTS book CASCADE'))
        conn.execute(text('DROP TABLE IF EXISTS publisher CASCADE'))
        conn.execute(text('DROP TABLE IF EXISTS shop CASCADE'))
def create_table(engine):
    Base.metadata.create_all(engine)


def find_publisher_sales(session):
    publisher_name = input('Введите имя издателя: ')

    query = text(
        """
        SELECT b.title AS book_title, s.name AS shop_name, sa.price, sa.date_sale
        FROM sale sa
        JOIN stock st ON sa.id_stock = st.id
        JOIN shop s ON st.id_shop = s.id
        JOIN book b ON st.id_book = b.id
        JOIN publisher p ON b.id_publisher = p.id
        WHERE p.name = :publisher_name
        """
    )

    sales = session.execute(query, {"publisher_name": publisher_name}).fetchall()

    if sales:
        print("Название книги | Название магазина | Стоимость покупки | Дата покупки")
        for sale in sales:
            print(
                f"{sale.book_title} | {sale.shop_name} | {sale.price} | {sale.date_sale.strftime('%d-%m-%Y')}"
            )
    else:
        print("Нет данных о продажах для этого издателя.")