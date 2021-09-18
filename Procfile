web: gunicorn pyfichepaie.wsgi --log-file -
celery: celery worker -A pyfichepaie -l info -c 4
