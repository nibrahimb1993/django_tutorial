# Django tutorial

## Requirements

- Broker for Celery (RabbitMQ or Redis), we are using RabbitMQ from docker image.

## Commands
- To create user run in shell: `python manage.py createsuperuser`
- To update `requirements.tx` file: `pip freeze-> requirements.txt`, and to install from it: `pip install -r requirements.txt`
- To migrate: `python manage.py migrate`
- To create migration file: `python manage.py makemigrations`
- To create virtual env: `python -m venv venv`, and to activate it: `source venv/bin/activate
`, and to deactivate it: `deactivate`

