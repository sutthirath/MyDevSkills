from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('skills/', views.skills_index, name='skills_index'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login_view'),
    path('welcome/', views.welcome, name='welcome'),
]