from django.urls import path
from . import views

urlpatterns =[
    path('', views.user_account , name="user_account"),
    path('register/', views.register, name="register"),
    path('login/', views.login_post, name="login"),
    path('profile/', views.profile, name="profile"),
    path('logout/', views.logout_post, name="logout"),
]