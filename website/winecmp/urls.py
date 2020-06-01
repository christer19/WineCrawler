from django.urls import path
from . import views
from django.views.generic import RedirectView
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(url='/login')),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('home/', views.homePage, name='home'),
    path('register/', views.registerPage, name='register')
]