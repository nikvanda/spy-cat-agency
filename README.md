To run this app you need:

Python3.12

Create venv:
Linux/MacOS:
```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

Windows:
```bash
$ python -m venv venv
$ venv\Scripts\activate
```

After creating venv you should install all requirements:
```
$ pip install -r requirements.txt
```

Apply all migrations:
Windows:
```bash
python manage.py makemigrations
python manage.py makemigrations agency_tasks_app
python manage.py migrate
```

Linux/MacOS:
```bash
python3 manage.py makemigrations
python3 manage.py makemigrations agency_tasks_app
python3 manage.py migrate
```

Run the app:
Windows:
```bash
python manage.py runserver 0.0.0.0:8000
```
Linux/MacOS:
```bash
python3 manage.py runserver 0.0.0.0:8000
```
