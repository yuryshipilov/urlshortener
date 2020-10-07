from django.contrib import admin
from django.urls import path
from authentication.views import home, login, signup
from django.contrib.auth import logout 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('login/', login, name='login'),
    path('signup/', signup, name='signup'),
    path('logout/', logout, name='logout'),
]
