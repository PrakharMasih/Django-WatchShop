from django.contrib import admin
from django.urls import path, include
from . import views
from django.conf.urls.static import static
# from views import Cart

urlpatterns = [
    # path('home/', views.home , name='home'),
    path('signup/', views.signup, name='signup'),
    path('', views.signin, name='signin'),
    path('1/', views.one, name='one'),
    path('2/', views.two, name='two'),
    path('3/', views.three, name='three'),
    path('4/', views.four, name='four'),
    path('5/', views.five, name='five'),
    path('6/', views.six, name='six'),
    path('7/', views.seven, name='seven'),
    path('8/', views.eight, name='eight'),
    path('index/', views.index, name='index'),
]
