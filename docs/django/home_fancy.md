# home page app fancy version

- quick and dirty home page that has some dynamic features
- makes routing initial urls to apps automatic
- lists folders in your django app
- excludes ones you do not want urls for
- creates urls to `your_apps/`
- start app

```sh
python manage.py startapp home 
```

- rout in your initial urls.py

```py
from home import views

    path('', views.homepage, name='home'),

```

- home/views.py

```py
from django.shortcuts import render
from django.http import HttpResponse
from automation.gadget import findviews, getmodule, cleanlist

import os

def homepage(request):
    folders = next(os.walk('.'))[1]
    excluded = ['home',
                'testui',
                'sandbox',
                'snippets',
                'static',
                'tests',
                ]
    folders = [f for f in folders if f not in (excluded)]
    folders = sorted(folders)
    html = """
            <h4>tests topics</h4>
            """
    for folder in folders:
        html += "<a class=\"mdl-button \" href=%s>%s</a>   " % (
            folder, folder)
    # return HttpResponse(html)
    return render(request, 'home/home.html', {'html':html})
```

- automation.gadget.py

```py
import inspect
import imp

def getmodule(path):
    name = inspect.getmodulename(path)
    return name

def findviews(path):
    """input view.py path output links to pages (function name)"""
    path = imp.load_source("__inspected__", path)
    all_functions = inspect.getmembers(path, predicate=inspect.isfunction)
    if(all_functions):
        all_functions = sorted(all_functions)
        return all_functions
    else:
        return('no views found')


def cleanlist(item_list, exclude):
    """convert inspect tuple to list and apply exclude list"""
    # convert tuple to list
    list_string = []
    for item in item_list:
        list_string.append(item[1].__name__)
    # apply exclusions
    clean_list = []
    for e in list_string:
        if e not in exclude:
            clean_list.append(e)
    item_list = clean_list
    return clean_list

def cleanhomelist(item_list, exclude):
    pass

if __name__ == '__main__':
    pass
```

- home.html

```html
{% extends "base.html" %} {% block title %}Homepage{% endblock %} {% block content %}
{{html|safe}}
<hr>
<br>
{% endblock %}
```
