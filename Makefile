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
	./venv/bin/python3 -m fliplearn
	# uvicorn app:app --reload
clean:
	rm -rf ./venv/