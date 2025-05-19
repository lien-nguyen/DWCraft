Chapter 1: Project Initialization
=================================
- Decided on a modular Django project structure based on the scaffold of project structure.


- Setup Docker and Docker Compose for consistent development environments.

- Installed Django and created the project with the correct folder structure.

- Installed Django and created the project with the correct folder structure.

  .. code-block:: bash

     # Install Django (in your virtual environment) prior to running the docker-compose command
     # This is a one-time setup step.
     # You can also use pipenv or poetry to manage your dependencies.
     pip install django==5.0.7

     # If plan to build nay APIs with Django Rest Framework, install it as well.
     pip install djangorestframework==3.15.0
     
     # django-app container is likely failing because manage.py does not exist yet. 
     # The command python manage.py runserver 0.0.0.0:8000 will fail if the Django project 
     # hasn’t been created.

     # Start a new Django project in the current directory (for me this is build2teach)
     django-admin startproject dwh_course .

     # Create the core app (as an example)
     python manage.py startapp core

     # Your folder structure should look like:
     #
     # build2teach/
     # ├── core/
     # ├── dwh_course/
     # ├── manage.py
     # └── requirements.txt

     # Next steps after creating the app:
     # Add 'core' to your INSTALLED_APPS in settings.py.
     # Create a simple view and URL for your homepage.
     # Test that your app is working by visiting the homepage.

     In core/urls.py (create this file):

     In core/urls.py (create this file):

     Visit http://localhost:8000 — you should see “Hello, DWCraft!”
   
    Recommended next steps:

    Set up templates for your core app

    Create a folder: build2teach/core/templates/core/
    Add a file: home.html with some HTML content.
    Update core/views.py to render this template using render(request, "core/home.html").
    Add a shared base template

    Create: build2teach/templates/base.html
    Use template inheritance in your app templates.
    Set up static files

    Place CSS/images in static
    Reference them in your templates.
    Configure PostgreSQL

    Update DATABASES in settings.py to use your Docker Postgres service.
    Run migrations:
    Create a superuser

    Then log in at /admin.

    Start scaffolding your next app

    For example, blog or course using:
