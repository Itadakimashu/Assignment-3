
from django.contrib import admin
from django.urls import path

from meal.views import home,show_meals
from about_us.views import about

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('show_meals/',show_meals,name='show_meals'),
    path('about/',about,name = 'about'),
]
