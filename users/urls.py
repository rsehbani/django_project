from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.sign_in, name='login'),
    path('session/', views.set_session),
    path('logout/', views.sign_out, name='logout'),
    path('register/', views.sign_up, name='register'),
]