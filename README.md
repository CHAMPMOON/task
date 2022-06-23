# Task


## Setup

Clone the repository:

```sh
$ git clone https://github.com/CHAMPMOON/task.git
$ cd task/
```

Create a virtual environment:

```sh
$ python -m venv env
$ source env/bin/activate
$ pip install -r requirements.txt
````

Create .env file similar example.env:

```sh
$ cp example.env .env
````

Do Database migrations:

```sh
$ python manage.py makemigrations
$ python manage.py migrate
```

Run development server:

```sh
$ python manage.py runserver
```

## Usage

* Load data into database from json file

```sh
$ python manage.py load_data
```

* Open `http://127.0.0.1:8000/data/`

![image](https://user-images.githubusercontent.com/72620861/175265129-db94455a-7baf-4e49-8d75-a24fd111f31a.png)


