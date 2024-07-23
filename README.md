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
django-admin startproject myProject
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
After running this if you go to "HTTP://localhost:8000" You will get the below-given page running in your localhost.
![](./Capture.PNG)
# 6. Creating a new app
To create your app, make sure you’re in the same directory as manage.py and type this command:
```
python manage.py startapp projectApp
```
# 7. Add the new app to the project
By adding app path in urls.py of project folder (myProject).
```
from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    # Enter the app name in following
    # syntax for this to work
    path('', include("projectApp.urls")),        # newly added line
]
```
# 7. Database setup
In settings.py update the database as Postgresql
```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "mydatabase",
        "USER": "mydatabaseuser",
        "PASSWORD": "mypassword",
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```
