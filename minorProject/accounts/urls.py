from django.urls import path
from accounts import views                           #take care this line
urlpatterns = [
    path('signin', views.signin, name='signin'),             
    path('login', views.login, name='login'),             
    path('logout', views.logout, name='logout'),                      
]