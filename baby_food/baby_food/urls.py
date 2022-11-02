
from django.contrib import admin
from django.urls import path, include

import baby_food.settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('baby_food.menu_app.urls')),
]
