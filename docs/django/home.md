# home page app

- quick and dirty home page routing
- start app

```sh
python manage.py startapp home 
```

- add to your starting point urls.py

```py
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.homepage),
]
```

- home/views.py  

```py
from django.shortcuts import render
from datetime import datetime

def homepage(request):
    this_date = datetime.now()
    this_date = this_date.strftime('year %Y week %U day %j')
    html = """
        """
    return render(request, 'home.html', {'html':html,'today':this_date})
```

- templates/home.html

```html
{% extends "base.html" %} {% block title %} Menu {% endblock %} {% block content %} 
<div class="container">
    <div class="row m-5 p-3">
        <div class="col">
            <h3>microapps</h3>
            <a href="boop"
                role="button" 
                class="btn btn-light m-3" mr-1>boop</a>
        </div>
    </div>
    <div class="row m-5 p-3">
        <div class="col">
        <a href="./blog/"
            role="button" class="btn btn-light mr-1 m-3">blog folder</a>
        <hr /> {{today|safe}}
        </div>
    </div>
</div>
{% endblock %}
```

- 404.html

```html
<html>
  <head>
    <title>Page Not Found</title>
  </head>
  <body bgcolor="#ffffff">
    <hr>
    <h1>404</h1><br><a href="{{ request.get_host }}/">bird up!</a>
    <hr>
  </body>
</html>
```

- 403.html

```html
<html>
  <head>
    <title>Page Not Found</title>
  </head>
  <body bgcolor="#ffffff">
    <hr>
    <h1>403</h1><br><a href="{{ request.get_host }}/">bird up!</a>
    <hr>
  </body>
</html>
```

- 500.html

```html
<html>
  <head>
    <title>Page Not Found</title>
  </head>
  <body bgcolor="#ffffff">
    <hr>
    <h1>500</h1><br><a href="{{ request.get_host }}/">bird up!</a>
    <hr>
  </body>
</html>
```

- base.html

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta
      charset="utf-8"
      name="viewport"
      content="width=device-width, initial-scale=1" />
    <title>{% block title %}{% endblock %}</title> 
    {% include "head.html" %} 
    {% block extrahead %}
    {% endblock %}
  </head>
  <body> {% include "nav.html" %} <div class="container text-center"> {% block content %}{% endblock %} </div>
    <!-- {% include "menu.html" %} -->
    <!-- #include file="footer.html" -->
    <script
      src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.1/dist/js/bootstrap.bundle.min.js"
      integrity=""
      crossorigin="anonymous"></script>
    <script
      src="https://code.jquery.com/jquery-1.12.4.min.js"
      integrity=""
      crossorigin="anonymous"></script>
  </body>
</html>
```
