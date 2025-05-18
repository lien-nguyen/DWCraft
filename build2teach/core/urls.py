from django.urls import path 
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    #path("about/", views.about, name="about"),
    #path("contact/", views.contact, name="contact"),
    #path("courses/", views.courses, name="courses"),
    #path("course/<int:course_id>/", views.course_detail, name="course_detail"),
]