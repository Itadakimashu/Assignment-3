from django.contrib import admin
from django.urls import path,include

import navigation.urls
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homepage),

    path('navigation/', include(navigation.urls))
]
