from django.urls import path
from .views import *


urlpatterns = [
   path('', post_list, name="post_list"),
   path('abot/',about,name="about"),
   path('contact/',contact,name="contact"),


]
