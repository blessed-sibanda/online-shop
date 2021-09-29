# Online Shop

A django online shop

## Features

- Customers can browse products, add them to the cart, apply discount codes, go through the checkout process, pay with credit card, and obtain an pdf invoice

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

### Install RabbitMQ

Make sure you have docker installer. If not, you can install docker [here](https://docs.docker.com/get-docker/). Run the RabbitMQ docker image using the following command.

```
$ docker run -it --rm --name rabbitmq -p 5672:5672 -p 15672:15672 rabbitmq:3.9-management
```

On another terminal launch celery
```
$ celery -A config worker -l info
```

On another teminal launch flower (to monitor celery)
```
$ celery -A config flower 
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
s