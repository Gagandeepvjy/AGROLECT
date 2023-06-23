from django.urls import path
from HOME import views

urlpatterns = [
    path('',views.home),
    path('contact/',views.contact,name='contact'),
    path('about/',views.about,name="about")
]
