from django.urls import path
from .views import create, create_business,create_professional,create_user

urlpatterns = [
    path('create',create,name="create"),
    path('create/user',create_user,name="create_user"),
    path('create/business',create_business,name="create_business"),
    path('create/professional',create_professional,name="create_professional")         
]