from django.contrib import admin
from django.urls import path, include
from home.views import home_page
from principal.views import user_login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('principal/', include('principal.urls')),
    path("", home_page ,name="home")

]

