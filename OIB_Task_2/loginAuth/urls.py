from django.urls import path
from loginAuth.views import *

urlpatterns = [
    path('signup',signup,name='signup'),
    path('index',index,name='index'),
    path('home',home,name='home'),
    path('logout',LogoutPage,name='logout'),
    path('save',save,name='save'),
]