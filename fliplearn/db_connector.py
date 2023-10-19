class FlipLearnPostgresql:
    def __init__(self):
        self.database = 'worldofi_fliplearn'
        self.cards_tb = 'worldofi_fliplearn_cards'
        self.users_tb = 'worldofi_fliplearn_users'

    def get_user_token_if_user_exists(self, username, password):
        ...

    def save_username_password(self, username, password):
        ...

    def save_card(self, user_id, card_front, card_back):
        ...

    def connect_to_db(self):
        ...

    def get_current_users_cards(self):
        ...
