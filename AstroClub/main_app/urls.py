from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name="profile"),
    path('accounts/', views.login, name="login"),
    path('accounts/signup', views.signup, name="signup"),
    path('intro_one/', views.intro_one, name="intro_one"),
    path('intro_two/', views.intro_two, name="intro_two"),
    path('intro_three/', views.intro_three, name="intro_three"),



    path('add_photo/', views.add_photo, name='add_photo')
]