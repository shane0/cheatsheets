---
tags:
  - django 
  - folders and files 
---
# folders and files

- quick and dirty way to serve static files
- folders and files on a django site
- combine with tools to convert markdown to htlm
- pandoc, pandas, revealjs, etc.
- run manually or in pipelines
- serve files using rsync, ftp or dropbox folders

## `pythonanywhere/pythonanywhere/urls.py`

```py
from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', views.homepage),
    path(r'blog/', include('mdblog.urls')),
]
```

## `pythonanywhere/pythonanywhere/urls.py`

```py
""" mdblog urls"""
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.blog, name='blog'),
    path('<folder>/', views.view_folder),
    path('<folder>/<file>', views.view_file)
]     
```

## `pythonanywhere/mdblog/views.py`

```py
from django.shortcuts import render
from django.http import HttpResponse 
import glob
import os
from django.conf import settings

MDBLOGFOLDER = os.path.join(settings.BASE_DIR, "whereveryouwant/")
MDPAGES = glob.glob(MDBLOGFOLDER + '/*/')

def blog(request):
    """return blog folders"""
    directories = next(os.walk(MDBLOGFOLDER))[1]
    return render(request, 'mdblog/directories.html', {'directories':directories})

def file_get_contents(filename):
    """contents of one file"""
    with open(filename, 'r',encoding="utf-8") as f:
        return f.read()

def view_folder(request,folder):
    """list files in one folder"""
    folder = MDBLOGFOLDER + folder
    html = "" #r"<h3>%s</h3>" % folder
    html += "<ul>"
    if os.path.isdir(folder):
        onlyfiles = [f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))]
        for f in onlyfiles:
            html += ("<li>\n")
            html += "<a href=%s>%s</a>" % (f, f)
            html += ("</li>\n")
    else:
        html += f"<br>folder: {folder} is empty"
    html += "</ul>"
    return render(request, 'mdblog/folder.html', {
        'html': html,
        'folder': folder,
        })

def view_file(request, folder, file):
    """show one file"""
    html = "" #r"<h3>%s</h3>" % folder
    html += '<h3>%s</h3>' % file
    contents = file_get_contents(MDBLOGFOLDER + '/' + folder + '/' + file)
    html_end = "" #"<a class=\"mdl-button mdl-js-button mdl-button--raised mdl-js-ripple-effect \"\ href=%s>%s</a>" % ('', 'run')
    return render(request, 'mdblog/file.html', {
        'html':html,
        'html_end':html_end,
        'contents': contents})
```
