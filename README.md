# Online Shop

A django online shop

## Features

- Customers can browse products, add them to the cart, apply discount codes, go through the checkout process, pay with credit card, and obtain an invoice

- Recommendation engine to recommend products to customers

- Internationalization to enable multiple languages in the site

## Setup Instructions

### Install [Git](https://git-scm.com/downloads)

Clone this repo and `cd` into it

```bash
$ git clone https://github.com/blessed-sibanda/online-shop
$ cd online-shop
```

### Install [Python](https://python.org/downloads) (version 3.8 or later)

Install pipenv using pip

```bash
$ pip install --user pipenv
```

Create a pipenv virtual environment

```bash
$ pipenv shell --python 3.8
```

Install pip dependencies

```bash
(online-shop) $ pipenv install
```

### Install [PostgreSQL](https://www.postgresql.org/download/)

After installing postgresql (using the above link), open `psql` shell

```bash
$ sudo su - postgres
$ psql
```

Create database

```psql
postgres=# CREATE DATABASE online_shop;
postgres=# CREATE USER online_shop;
postgres=# GRANT ALL ON DATABASE online_shop to "online_shop";
postgres=# ALTER USER online_shop PASSWORD '1234pass';
postgres=# ALTER USER online_shop CREATEDB;
postgres=# \q;
```

Exit postgresql shell

```bash
$ exit
```

Run database migrations (in project root folder)

```bash
(online-shop) $ python manage.py migrate
```

Create a superuser account

```bash
(online-shop) $ python manage.py createsuperuser
```

Open the application in your browser at [http://127.0.0.1:8000](http://127.0.0.1:8000)
