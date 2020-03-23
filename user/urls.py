from django.urls import path
from django.contrib.auth import views as auth_views

from user import views

app_name='user'

urlpatterns=[

    path('register',views.createuser,name='register'),
    path ('',views.login_user,name='login'),
    path('logout/',views.logout_user,name='logout'),
]