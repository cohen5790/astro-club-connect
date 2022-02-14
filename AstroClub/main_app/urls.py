from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name="profile"),
    path('accounts/', views.login, name="login"),
    path('accounts/signup', views.signup, name="signup"),



    path('add_photo/', views.add_photo, name='add_photo')
]