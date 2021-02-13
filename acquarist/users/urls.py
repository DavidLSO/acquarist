from django.urls import path

from acquarist.users import views


urlpatterns = [
    path('', views.user_create, name='user-create'),
    path('profile/', views.user_update, name='user-profile'),
]
