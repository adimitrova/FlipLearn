import os
import pathlib
import sqlite3
from typing import Tuple

FLIPLEARN_DB = 'database/fliplearn.db'
CARDS_TB = 'fliplearn_cards'
USERS_TB = 'fliplearn_users'
COLLECTIONS_TB = 'fliplearn_collections'

EXPECTED_TABLES = [CARDS_TB, USERS_TB, COLLECTIONS_TB]


class FlipLearnDB:
    def __init__(self):
        self.connection, self.cursor = self.connect_to_db()
        if not self.db_contains_all_required_tables:
            self.setup_db_and_tables()

    def setup_db_and_tables(self):
        self.cursor.execute(f'''
                  CREATE TABLE IF NOT EXISTS {USERS_TB}
                  ([user_id] TEXT PRIMARY KEY, 
                  [username] TEXT, 
                  [password] TEXT, 
                  [email_address] TEXT, 
                  [first_name] TEXT, 
                  [last_name] TEXT,
                  [agree_to_terms] BOOLEAN,
                  [registration_date] timestamp,
                  [collection_id] TEXT)
                  ''')

        self.connection.commit()

    @property
    def db_contains_all_required_tables(self):
        return False

    @property
    def db_exists(self) -> bool:
        os.makedirs(pathlib.Path(FLIPLEARN_DB).parent, exist_ok=True)
        if os.path.exists(FLIPLEARN_DB):
            return True
        return False

    def check_tables(self):
        self.cursor.execute(f'''
            SELECT name FROM sqlite_master WHERE type='table';
        ''')
        print(self.cursor.fetchall())

    def get_user_token_if_user_exists(self, username, password):
        ...

    def save_username_password(self, username, password):
        ...

    def save_card(self, user_id, card_front, card_back):
        ...

    def connect_to_db(self) -> Tuple[sqlite3.Connection, sqlite3.Cursor]:
        self.connection = sqlite3.connect(FLIPLEARN_DB)
        self.cursor = self.connection.cursor()
        return self.connection, self.cursor

    def get_current_users_cards(self):
        ...


if __name__ == "__main__":
    fldb = FlipLearnDB()
    fldb.check_tables()
