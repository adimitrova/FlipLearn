install:
	uv sync

run:
	uv run python manage.py runserver

migrate:
 	# if you move from another computer or do a fresh install of the app, run this command
	uv run python manage.py makemigrations
	uv run python manage.py migrate --run-syncdb

clean:
	rm -rf venv/

backup_db:
	sqlite3 flash_cards_db_backup.sq3 ".backup 'backup/flash_cards_db_backup_$(date "+%Y-%m-%d").sq3'"

create_superuser:
	uv run python manage.py createsuperuser

get_query_console:
	uv run python manage.py shell