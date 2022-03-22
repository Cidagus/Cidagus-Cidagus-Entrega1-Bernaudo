from django.urls import path
from .views import create, create_business,create_professional,create_user,search,search_business,search_professional,search_user

urlpatterns = [
    path('create',create,name="create"),
    path('create/user',create_user,name="create_user"),
    path('create/business',create_business,name="create_business"),
    path('create/professional',create_professional,name="create_professional"),
    
    path('search',search,name='search') ,
    path('search/user',search_user,name='search_user'),
    path('search/business',search_business,name='search_business'),
    path('search/professional',search_professional,name='search_professional')
            
]