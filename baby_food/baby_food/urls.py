from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import baby_food.settings

urlpatterns = [
    path('bf-admin/', admin.site.urls),
    path('', include('baby_food.common.urls')),
    path('accounts/', include('baby_food.accounts.urls')),
    path('menu_app/', include('baby_food.menu_app.urls')),
    path('recipes/', include('baby_food.recipes.urls')),
    path('cart/', include('baby_food.cart.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)