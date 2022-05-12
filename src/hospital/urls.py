from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('account.urls', namespace="account")),
    path("", include('user_profile.urls', namespace="user_profile")),
    path("", include('appointment.urls', namespace="appointment")),
    path('drugs/', include('drugs.urls', namespace='drugs')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
