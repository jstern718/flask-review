Dev Server
$ flask --app flaskr run --debug

Deployment
$ pip install build
$ python -m build --wheel

Testing

$ pytest
$ pytest -v
$ coverage run -m pytest
$ coverage report
$ coverage html --> htmlcov/index.html