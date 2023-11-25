import datetime
import os
import pathlib
import sqlite3
import uuid
from typing import Tuple

from fliplearn.contracts import User

FLIPLEARN_DB = 'database/fliplearn.db'
CARDS_TB = 'fliplearn_cards'
USERS_TB = 'fliplearn_users'
COLLECTIONS_TB = 'fliplearn_collections'

EXPECTED_TABLES = [CARDS_TB, USERS_TB, COLLECTIONS_TB]


class FlipLearnDB:
    def __init__(self):
        self.connection = self.cursor = None

    def connect_and_disconnect_to_db(run_method):
        def decorated_method(self, *args, **kwargs):  # NB! here passing potential args and kwargs
            try:
                # Start a new connection
                self.connection, self.cursor = self._connect_to_db()

                # Execute whatever is required
                run_method(self, *args, **kwargs)  # self is important, otherwise errors
            finally:
                # close connection
                self.cursor.close()
                self.connection.close()

        return decorated_method

    @connect_and_disconnect_to_db
    def setup_db_and_tables(self):
        if not self.db_contains_all_required_tables:
            self.cursor.execute(f'''
                      CREATE TABLE IF NOT EXISTS {USERS_TB}
                      ([user_id] TEXT PRIMARY KEY, 
                      [username] TEXT, 
                      [password] TEXT, 
                      [email_address] TEXT, 
                      [first_name] TEXT, 
                      [last_name] TEXT,
                      [agree_to_terms] BOOLEAN,
                      [registration_date] timestamp)
                      ''')
            self.cursor.execute(f'''
                              CREATE TABLE IF NOT EXISTS {CARDS_TB}
                              ([card_id] TEXT PRIMARY KEY, 
                              [user_id] TEXT, 
                              [collection_id] TEXT, 
                              [tag] TEXT, 
                              [front_side] TEXT, 
                              [back_side] TEXT)
                              ''')
            self.cursor.execute(f'''
                              CREATE TABLE IF NOT EXISTS {COLLECTIONS_TB}
                              ([collection_id] TEXT PRIMARY KEY, 
                              [collection_title] TEXT, 
                              [user_id] TEXT)
                              ''')
            self.connection.commit()

    @connect_and_disconnect_to_db
    @property
    def db_contains_all_required_tables(self):
        return False

    @property
    def db_exists(self) -> bool:
        os.makedirs(pathlib.Path(FLIPLEARN_DB).parent, exist_ok=True)
        if os.path.exists(FLIPLEARN_DB):
            return True
        return False

    @connect_and_disconnect_to_db
    def fetch_available_tables(self):
        self.cursor.execute(f'''
            SELECT name FROM sqlite_master WHERE type='table';
        ''')
        print(self.cursor.fetchall())

    @connect_and_disconnect_to_db
    def insert_new_user(self, user: User):
        self.cursor.execute(f"""
            INSERT INTO {USERS_TB} 
                (user_id, username, password, email_address, 
                first_name, last_name, agree_to_terms, registration_date)
            VALUES ([{user.user_id}], {user.username}, {user.password}, [{user.email_address}], 
                    {user.first_name}, {user.last_name}, {user.agree_to_terms}, 
                    datetime('now'))
        """)

    @connect_and_disconnect_to_db
    def get_user_token_if_user_exists(self, username, password):
        ...

    @connect_and_disconnect_to_db
    def save_username_password(self, username, password):
        ...

    @connect_and_disconnect_to_db
    def save_card(self, user_id, card_front, card_back):
        ...

    def _connect_to_db(self) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
        # NB! Connect to a database file if exists otherwise create it at the specified location
        self.connection = sqlite3.connect(FLIPLEARN_DB)

        self.cursor = self.connection.cursor()
        return self.connection, self.cursor

    @connect_and_disconnect_to_db
    def get_current_users_cards(self):
        ...


# TODO: delete when done testing this class
def temp_main():
    fldb = FlipLearnDB()
    fldb.setup_db_and_tables()

    fldb.fetch_available_tables()

    user = User(
        user_id=str(uuid.uuid4()).split('-')[-1],
        username='anid',
        password='blabla',
        first_name='ani',
        last_name='dimi',
        email_address='ani@email.com',
        agree_to_terms=True,
        registration_date=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    )

    fldb.insert_new_user(user)


if __name__ == "__main__":
    temp_main()
