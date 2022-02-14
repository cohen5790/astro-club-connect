from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name="profile"),
    path('matches/', views.matches, name="matches"),
    path('accounts/', views.login, name="login"),
    path('accounts/signup', views.signup, name="signup"),
    path('intro_one/', views.intro_one, name="intro_one"),
    path('intro_two/', views.intro_two, name="intro_two"),
    path('intro_three/', views.intro_three, name="intro_three"),
    path('questions_one/', views.questions_one, name="questions_one"),
    path('questions_two/', views.questions_two, name="questions_two"),
    path('questions_three/', views.questions_three, name="questions_three"),
    path('questions_matches/', views.questions_matches, name="questions_matches"),



    path('add_photo/', views.add_photo, name='add_photo')
]