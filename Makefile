setup: requirements.txt
	createdb dev-fake-support
	python -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt
	flask db init


run: fake_support.py
	flask run --port 3001

clean:
	rm -rf __pycache__
