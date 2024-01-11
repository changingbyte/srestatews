from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from . import settings

from main.views import IndexPageView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexPageView.as_view(), name='index'),

    path('i18n/', include('django.conf.urls.i18n')),

    path('accounts/', include('accounts.urls')),

    path("chat/", include("chat.urls"))
]

urlpatterns += staticfiles_urlpatterns(settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
