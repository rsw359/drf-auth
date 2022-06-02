# Lab 32

## Project: DRF Auth

## Author: Roger Wells

### Links and Resources

[Github](https://github.com/rsw359/drf-auth/blob/main/README.md)

### To run this application

- Clone the repo into you directory
- create virtual environment and activate:
  - python -m venv .venv
  - source venv/bin/activate
- create django project

- Install Depencies:
  - pip install django
  - pip install djangorestframework
  - pip install djangorestframework-simplejwt
  - pip install psycopg2
  - pip install gunicorn
  - pip install whitnoise

- Django commands
  - python manage.py:
    - migrate
    - runserver

- Go to localhost:8000/api/v1/bike

 For testing:

- run: python manage.py test
- For testing in Thunderclient:
  - go to localhost:8000/api/token
  - login
  - copy the jwt token
  - IN VSCODE: open thunderclient
  - select collections/newcollection/*choose name*
    - for get token:
    - for refresh token:
    - for create: choose POST