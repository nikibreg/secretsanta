## Running Locally

Make sure you have Python 3.7 [installed locally](http://install.python-guide.org).

```sh
$ git clone https://github.com/nikibreg/secretsanta.git
$ cd secretsanta

$ pip install -r requirements.txt
$ python manage.py migrate
$ python manage.py collectstatic
$ python manage.py runserver
```

Your app should now be running on [localhost:8000](http://localhost:8000/)