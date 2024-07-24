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
By adding app path in urls.py inside the project folder (myProject).
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
Now You can use the default MVT model to create URLs, models, views, etc. in your app and they will be automatically included in your main project.
# 8. Create urls.py in the App folder
Include the following code
```
from django.urls import path
#now import the views.py file into this code
from . import views
urlpatterns=[
path('',views.index)
]
```
The above code will call or invoke the function which is defined in the views.py file so that it can be seen properly in the Web browser. Here it is assumed that views.py contains the following code :-
```
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello Geeks")
```
After adding the above code, go to the settings.py file which is in the project directory, and change the value of ROOT_URLCONF from ‘project.urls’ to ‘app.urls’
```
ROOT_URLCONF = 'app.urls'
```
And then you can run the server(127.0.0.1:8000) and you will get the desired output.

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
