<H1 align="center"> Django Application</H1>

## Steps To Start a Django Application

**1. Install Django**

```
python -m pip install Django
```
[`Reference Link`](https://docs.djangoproject.com/en/5.0/topics/install/#installing-official-release)

**2. Verify Django Installation**
```
python -m django --version
```
If Django is installed, you should see the version of your installation. If it isn’t, you’ll get an error telling “No module named Django”.

**3. Creating a new project**
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

**4. Run the server**

Run the command in the terminal to run our Django server.
```
python manage.py runserver
```
After running this if you go to "HTTP://localhost:8000" You will get the below-given page running in your localhost.
![](./Capture.PNG)


**5. Creating a new app**

To create your app, make sure you’re in the same directory as manage.py and type this command:
```
python manage.py startapp projectApp
```

**6. Add the new app to the project**

By adding app path in urls.py inside the project folder (myProject).
```
from django.contrib import admin
from django.urls import path, include
 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("projectApp.urls")),        # newly added line
]
```
Now You can use the default MVT model to create URLs, models, views, etc. in your app and they will be automatically included in your main project.

**7. Create urls.py in the App folder**

Include the following code in the urls.py for 
```
from django.urls import path

#now import the views.py file into this code
from . import views
urlpatterns=[
    path('', views.index, name='index'),
]
```

**8. Add the first index function for frontend in the views.py**

In Django, We will define all our frontend webpages as functions in views.py
The above code will call or invoke the function which is defined in the views.py file so that it can be seen properly in the Web browser. 

Add the following code in views.py of App directory:-
```
from django.http import HttpResponse

def index(request):
  return HttpResponse("Hello Geeks")
```
After adding the above code, go to the settings.py file which is in the project directory, and change the value of ROOT_URLCONF from ‘project.urls’ to ‘app.urls’
```
ROOT_URLCONF = 'mysite.urls'
```
And then you can run the server(127.0.0.1:8000) and you will get the desired output - "Hello Greeks".

**9. Create first index.html frontend**

- Create a Template Directory:
  
  Ensure you have a templates directory within your Django app directory. If you don't have one, create it.
  ```
  myapp/
    templates/
            index.html

  ```
- Add the Template Directory to Settings:
  
  In your Django project's settings.py, add the TEMPLATES directory if it's not already set up:
  Update the code as shown below
  ```
  TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],  # Ensure the 'templates' directory is included
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
    ]
  ```
  
- Create the index.html File:
  
  Create an index.html file within the templates/ directory.
    ```
    <!-- myapp/templates/myapp/index.html -->
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Index Page</title>
    </head>
    <body>
        <h1>Welcome to MyApp</h1>
    </body>
    </html>
    ```
    
- Create a View for the Index Page:
  
  In your app's views.py, create a view that will render the index.html template.
    ```
    from django.shortcuts import render
    
    def index(request):
        return render(request, 'index.html')
    ```

## <h2 align="center">Create Admin User and Sub Users in Django</h2>

**10. create an admin user**

To create an admin user in Django, follow these steps:

- Run the Create Superuser Command:
  Open your terminal and navigate to your Django project directory. Then run the following command:
  ```
  python manage.py createsuperuser
  ```
  
- Enter the Superuser Details:
  You will be prompted to enter a username, email address, and password for the superuser. Fill in the required details.
    ```
    Username: admin
    Email address: admin@example.com
    Password: **********
    Password (again): **********
    ```
    
- Access the Admin Interface:

    Start the Django development server if it's not already running, Open a web browser and navigate to http://127.0.0.1:8000/admin/. Use the superuser credentials you just created to log in.
  
## <h2 align="center">Create Management Software Using Django For An Educational Institution </h2>

**1. Install DataBase**

Install the Postgresql database and configure pgAdmin 4 in system, which is already installed. Create a new database.
[`Reference Link`](https://docs.djangoproject.com/en/5.0/topics/install/#database-installation)

**2. Set Up Django with PostgreSQL**

In settings.py update the database as your Postgresql

```
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "postgres",        # Your db name
        "USER": "postgres",        # Your db user name
        "PASSWORD": "Password",    # Your db password
        "HOST": "127.0.0.1",
        "PORT": "5432",
    }
}
```

**3. Create a Django Model for Table**

Define a model for the table you want to create. For example, if you want to create a table for storing student information:
```
# myapp/models.py
from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    enrollment_date = models.DateField()
    grade = models.CharField(max_length=10)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
```

**4. Add Your App to INSTALLED_APPS**

Open your project's settings.py and add your app (e.g., projectApp) to the INSTALLED_APPS list.

```
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'projectApp',          # Add your app here
]
```

**5. Create and Apply Migrations**

Generate and apply the migrations to create the table in the PostgreSQL database:

```
python manage.py makemigrations
python manage.py migrate
```

**6. Create a frontend View to Retrieve Data**

Create a view to fetch data from the Student model and pass it to the template, in views.py in app folder.

```
# myapp/views.py
from django.shortcuts import render
from .models import Student

def student_list(request):
    students = Student.objects.all()
    return render(request, 'projectApp/student_list.html', {'students': students})

```

**7. Create a URL Pattern**

Add a URL pattern to route requests to the view in urls.py of app folder

```
# myapp/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('students/', views.student_list, name='student_list'),
]
```

**8. Create a frontend HTML Template to Display Data**

Create a template to display the data in an HTML table

```
<!-- myapp/templates/myapp/student_list.html -->
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Student List</title>
</head>
<body>
    <h1>Student List</h1>
    <table border="1">
        <thead>
            <tr>
                <th>First Name</th>
                <th>Last Name</th>
                <th>Enrollment Date</th>
                <th>Grade</th>
            </tr>
        </thead>
        <tbody>
            {% for student in students %}
            <tr>
                <td>{{ student.first_name }}</td>
                <td>{{ student.last_name }}</td>
                <td>{{ student.enrollment_date }}</td>
                <td>{{ student.grade }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>
</body>
</html>

```

**9. Run the Development Server**

Start the Django development server:

```
python manage.py runserver

```
Open a web browser and navigate to http://127.0.0.1:8000/students/ to view the student list table.


