#-*- coding: utf-8 -*-
from django.conf import settings
from django.urls import include, path
from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('mailer.urls')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),

    ] + urlpatterns
