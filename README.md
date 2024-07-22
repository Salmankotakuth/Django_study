<H1 align="center"> Django Application</H1>

## Steps To Start a Django Application
# 1. Install DataBase
[`Referenace Link`](https://docs.djangoproject.com/en/5.0/topics/install/#database-installation)
# 2. Install Django
```
python -m pip install Django
```
[`Referenace Link`](https://docs.djangoproject.com/en/5.0/topics/install/#installing-official-release)
# 3. Verify Django Installation
```
python -m django --version
```
If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error telling “No module named django”.
# 4. Creating a project
```
django-admin startproject mysite
```
This will create a mysite directory in your current directory.
Let’s look at what startproject created:
```
mysite/
    manage.py
    mysite/
        __init__.py
        settings.py
        urls.py
        asgi.py
        wsgi.py
```
# 5. The development server
```
python manage.py runserver
```
![](./capture.png)
