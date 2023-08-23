from django.contrib import admin
from .settings import STATIC_URL, STATICFILES_DIRS, MEDIA_URL, MEDIA_ROOT, LOCALES_URL, LOCALES_ROOT
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include('api.urls')),
	path('auth/', include('rest_framework.urls')),
	path('', include('frontend.urls'))
] + static(STATIC_URL, document_root=STATICFILES_DIRS)  + static(MEDIA_URL, document_root=MEDIA_ROOT) + static(LOCALES_URL, document_root=LOCALES_ROOT)
