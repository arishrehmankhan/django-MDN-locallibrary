[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)

# django-MDN-locallibrary
This repo contains the code of django locallibrary project which is used in the MDN docs django tutorial (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)

## About Repository
I made this repository when I was learning django from MDN. I have committed changes after every chapter and also completed all the challenges of the tutorial.
Feel free to refer the code if you are having problems in completing the challenges.

You can also pull this code to you local computer by following these steps given below.

## Technology Stack
* Django (Python)
* SQLite as DB

## Requirements 
* Any operating system (i.e. Linux, Windows, MacOS X)
* A little knowledge of Django. Don't worry if you are new to it, you just need knack to learn.
* Any IDE (i.e. VSCode, etc)

## Setting up the project
* Create a virtual environment in recently created directory and activate it:
```
python3 -m venv env
source env/bin/activate
```

You can also use another virtual environments for python which you prefer.

* Clone the repository and enter to the repository:
```
git clone https://github.com/arishrehmankhan/django-MDN-locallibrary.git
cd django-MDN-locallibrary
```

* Next, install the dependencies using pip:
```
pip install -r requirements.txt 
```
* Once the dependencies is installed, migrate your database.
```
python3 manage.py migrate
python3 manage.py makemigrations
```

* Then create a superuser account for Django:
```
python manage.py createsuperuser
```

* Finally, you’re ready to start the development server:
```
python manage.py runserver
```
Visit [localhost:8000](http://127.0.0.1:8000/) in your browser to see how it looks.
