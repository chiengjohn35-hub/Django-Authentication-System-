from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('profile/', views.profile, name="profile"),
    path('register/', views.register_post, name="register"),
    path('login/', views.login_post, name="login"),
    path('logout/', views.logout_post, name="logout"),
]


