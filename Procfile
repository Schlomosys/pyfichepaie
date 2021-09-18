web: gunicorn pyfichepaie.wsgi --log-file -
worker: python manage.py celery worker -B -l info
