from django.urls import path
from .views import homepage, blogpage

urlpatterns = [
     path("",homepage, name=("homepage")),
     path("blog",blogpage, name="blogpage")    
]