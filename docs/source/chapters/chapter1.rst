Chapter 1: Project Initialization
=================================
- Decided on a modular Django project structure based on the scaffold of project structure.


- Setup Docker and Docker Compose for consistent development environments.

- Installed Django and created the project with the correct folder structure.

- Installed Django and created the project with the correct folder structure.

  .. code-block:: bash

     # Install Django (in your virtual environment)
     pip install django==5.0.7

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