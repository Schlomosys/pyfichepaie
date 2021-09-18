web: gunicorn pyfichepaie.wsgi --log-file -
worker: celery -A pyfichepaie  worker -l info -c 4
