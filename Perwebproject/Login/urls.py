from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views
urlpatterns=[

    path('signup/', views.register, name='app-register'),
    path('profile/', views.profile, name='app-profile'),
    path('login/', auth_views.LoginView.as_view(), name='app-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name ='registration/logout.html'), name='app-logout'),

]