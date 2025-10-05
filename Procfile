release: python manage.py migrate && python manage.py create_demo_user
web: python manage.py migrate && python manage.py create_demo_user && gunicorn mi_proyecto.wsgi --bind 0.0.0.0:$PORT --workers 1