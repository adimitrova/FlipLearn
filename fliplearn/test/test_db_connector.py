import pytest as pytest

from ..db_connector import FlipLearnDB


class test_decorator(pytest):
    @FlipLearnDB.connect_and_disconnect_to_db
    def test_decorator_connect_and_disconnect_to_db(self):
        # see how to test decorators here https://stackoverflow.com/a/1263782
        ...
