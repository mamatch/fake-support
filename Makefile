setup: requirements.txt
	pip install -r requirements.txt
	export FLASK_APP=fake_support.py
	export DEBUG=1
	flask db init


run: fake_support.py
	flask run

clean:
	rm -rf __pycache__