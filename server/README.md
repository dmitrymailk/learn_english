# Server

- [create environment in windows](https://docs.python.org/3/library/venv.html)
- [powershel run command](https://www.howto-outlook.com/howto/powershell-scripts-faq-tips-and-tricks.htm)
- [save all libraries to requirements.txt](https://stackoverflow.com/questions/31684375/automatically-create-requirements-txt)
- [django tutorial](https://docs.djangoproject.com/en/3.2/intro/tutorial01/)
- [.env files django](https://dev.to/jakewitcher/using-env-files-for-environment-variables-in-python-applications-55a1)
- [delete app django](https://www.delftstack.com/howto/django/django-remove-app/)
- [solve django migrations problems](https://simpleisbetterthancomplex.com/tutorial/2016/07/26/how-to-reset-migrations.html)
- [free vocabulary api](https://dictionaryapi.dev/)
- [oxford vocabulary api](https://developer.oxforddictionaries.com/)

## Общие советы

- Если не проходит migrate прежде лучше проверить все приложения на makemigrrations и только потом пытаться совершать какие-то глобальные действия

## Code snippets

```plaintext
pip freeze > requirements.txt
```

```plaintext
pip install -r requirements.txt
```

```plaintext
python manage.py runserver 8080
```

```plaintext
python manage.py createsuperuser
```

```plaintext
python -m pip uninstall package_name
```

```plaintext
heroku logs -n 1500 --app english-card-test
```
