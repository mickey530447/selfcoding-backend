from django.urls import path
from .views import role_list,role_detail

urlpatterns = [
    path('roles/', role_list),
    path('roles/<int:pk>',role_detail),

]