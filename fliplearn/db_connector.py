import psycopg2
from sqlalchemy import create_engine, text


class FlipLearnDB:
    def __init__(self):
        self.database = 'worldofi_fliplearn'
        self.cards_tb = 'worldofi_fliplearn_cards'
        self.users_tb = 'worldofi_fliplearn_users'
        self.username = 'worldofi_mysql_admin'
        self.hostname = 'worldofinspiration.net'
        self.pwd = 'xxxxxxxx'

    def get_user_token_if_user_exists(self, username, password):
        ...

    def save_username_password(self, username, password):
        ...

    def save_card(self, user_id, card_front, card_back):
        ...

    def connect_to_db(self):
        connection_string = f"mysql+mysqlconnector://{self.username}:{self.pwd}@{self.hostname}:3306/sqlalchemy"
        engine = create_engine(connection_string, echo=True)
        with engine.connect() as connection:
            connection.execute(text("CREATE TABLE example (id INTEGER, name VARCHAR(20))"))
            connection.execute(text("SHOW tables"))

    def get_current_users_cards(self):
        ...


# if __name__ == "__main__":
#     fldb = FlipLearnDB()
#     fldb.connect_to_db()
