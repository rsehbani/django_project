from django.urls import path
from . import views
from .views import set_cookie, process_cookie, get_cookie

urlpatterns = [
    path('home', views.home, name='posts'),
  
    path('post/create', views.create_post, name='post-create'),
    path('post/edit/<int:id>/', views.edit_post, name='post-edit'),
     path('post/delete/<int:id>/', views.delete_post, name='post-delete'),
     path('visit/', views.count_visit, name='visit'),
     path('set_language/', views.set_language, ),
     path('get_language/', views.get_language),
     path('delete_language', views.delete_language_preference),
     path('setcookie/', views.set_cookie_view),
     path('getcookie/', views.get_cookie_view),
     path('deletecookie/',views.delete_cookie_view),
     path('acceptcookie/', views.accept_cookies, name='accept_cookies'),
     path('set_cookie/', set_cookie, name='set_cookie'),
    path('process_cookie/', process_cookie, name='process_cookie'),
    path('get_cookie/', get_cookie, name='get_cookie'),
    path('', views.about, name='about'),

]
