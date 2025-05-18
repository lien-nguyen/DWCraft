Setup Guide
===========

This guide summarizes the steps to set up the build2teach project.

1. **Clone the repository**  
   Clone the project to your local machine.

2. **Project Structure**  
   The main structure is:
   ::
   
       build2teach/
         ├── core/
         ├── blog/
         ├── course/
         ├── users/
         ├── static/
         ├── templates/
         ├── manage.py
         ├── requirements.txt
         ├── docker-compose.yml
         ├── Dockerfile
         └── dwh_course/
             ├── __init__.py
             ├── settings.py
             ├── urls.py
             └── wsgi.py

3. **Install dependencies**  
   Add required Python packages to `requirements.txt` (e.g., Django, djangorestframework, psycopg2-binary, markdown, sphinx).

4. **Build and run Docker containers**
   ::
   
       docker compose build
       docker compose up

5. **Create Django apps**  
   Use `python manage.py startapp <appname>` for each app (core, blog, course, users).

6. **Set up Sphinx documentation**  
   ::
   
       pip install sphinx
       sphinx-quickstart docs

7. **Build documentation**  
   ::
   
       cd docs
       make html

8. **View documentation**  
   Open `docs/build/html/index.html` in your browser.
