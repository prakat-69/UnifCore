from django.urls import path
from .views import register_api , get_user_profile_api ,update_user_api

urlpatterns = [
    path('register/',register_api,name='Register User'),
    path("<int:user_id>/",get_user_profile_api,name='Get User Details by id'),
    path("update/<int:user_id>/",update_user_api,name='Update User Details by id')

]


