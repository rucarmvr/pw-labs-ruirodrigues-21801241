release: python3 manage.py migrate
python3 manage.py collectstatic --noinput
web: gunicorn config.wsgi:application --log-file - --log-level debug