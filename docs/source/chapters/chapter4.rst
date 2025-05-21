Chapter 4: Core App
===================================

-    Recommended next steps:
-   Set up templates for your core app
-    Create a folder: build2teach/core/templates/core/
-    Add a file: home.html with some HTML content.
-    Update core/views.py to render this template using render(request, "core/home.html").
-    Add a shared base template
-    Create: build2teach/templates/base.html
-   Use template inheritance in your app templates.
-    Set up static files
-    Place CSS/images in static
-    Reference them in your templates.
-    Configure PostgreSQL
-    Update DATABASES in settings.py to use your Docker Postgres service.
-    Run migrations:
-    Create a superuser
-    Then log in at /admin.
-    Start scaffolding your next app


.. code-block:: bash

    #1. Set up templates for your core app
    #a. Create the template folder and file:
    mkdir -p build2teach/core/templates/core
    echo "<h1>Welcome to build2teach!</h1>" > build2teach/core/templates/core/home.html
   
    # b. Update core/views.py to render the template:
    from django.shortcuts import render

    def home(request):
        return render(request, "core/home.html")

    # 2. Add a shared base template
    #a. Create the base template:
    mkdir -p build2teach/templates
    echo "{% block content %}{% endblock %}" > build2teach/templates/base.html

    # b. Update core/templates/core/home.html to extend the base template:
    {% extends "base.html" %}
    {% block content %}
    <h1>Welcome to build2teach!</h1>
    {% endblock %}

    # 3. Set up static files
    # Place your CSS/images in css and img.
    # Reference them in your templates:
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <img src="{% static 'img/logo.png' %}" alt="Logo">

    #4. configure PostgreSQL
    #a. Update DATABASES in settings.py to use your Docker Postgres service:
    DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": "django_db",
        "USER": "django",
        "PASSWORD": "django",
        "HOST": "django-db",
        "PORT": 5432,
    }
}