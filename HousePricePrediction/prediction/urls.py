from django.contrib import admin
from django.urls import path
from prediction import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('home/', views.home, name='home'),
    path('home/predict/', views.predict, name='predict'),
    path('home/predict/result/', views.result, name='result'),
    path('about/', views.about, name='about'),
    path('', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('login_success/', views.login_success, name='login_success'),
    path('login_failure/', views.login_failure, name='login_failure'),
    path('logout/', views.logoutPage, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
