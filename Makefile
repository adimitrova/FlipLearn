.MAIN: install

install:
	sudo apt-get install libpq-dev python-dev
	python3 -m venv venv
	chmod +x ./venv/bin/activate
	./venv/bin/activate
	pip install -r requirements.txt
run:
	./venv/bin/activate
	cd fliplearn/
	uvicorn fliplearn.app:app --reload
clean:
	rm -rf ./venv/