---
tags:
  - django 
---
# django

- i have a django site here that i tinker with
- <https://shane0.pythonanywhere.com/>
- see youtube link bottom of page
- I have some django screencasts
- use it for websites, front or back end
- django is a huge time saver
- has a bunch of stuff built in
- todo: put my django click app here

```sh
# django
alias dr='python manage.py runserver 8000'
alias vvv='virtualevn venv'
alias vv='source venv/bin/activate'
alias vf='pip install --editable .'
alias vr='pip install -r requirements.txt'
alias lt='ls --human-readable --size -1 -S --classify'
```

```sh
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py migrate --run-syncdb
```

## hosting

- pythonanywhere is free and works with a sqlite db
- if you want postgres you can use supabase for free
- pythonanywhere does not allow connecting to supabase unless you pay
- this was an annoying waste of time just to determine what the errors meant
- I had to dig into their forums to find a user that explained you have to pay to enable it
- side note about python anywhere: fastapi requires asgi & they only provide wsgi
- I've tried a few other ways to host django
- google cloud run
- aws
- linode & openlitespeed
- python anywhere is the only one I stuck with
