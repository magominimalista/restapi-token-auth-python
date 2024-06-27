#     My annotations

| OBS: At first install all dependencies and check the right name that has called, because it's can change between versions.

- The command to run server: `python3 manage.py runserver`
- First command: `python3 manage.py makemigrations`
- Second command: `python3 manage.py migrate`
- Install djangorestframework
- Run the command to create app rest_api: `python3 manage.py startapp rest_api`
- Remember to register on the settings.py and urls.py to the news routes
- After add token part, run Second command and to create a new user with token: `python manage.py create_token --username myuser --password mypass`