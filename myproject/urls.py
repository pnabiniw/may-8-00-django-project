from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("form/", include("form.urls")),
    path("crud/", include("crud.urls")),
    path("classbased/", include("classbased.urls")),
    path("api/", include("api.urls")),
    path("api-crud/", include("api_crud.urls")),
    path("", include("account.urls")),
    path("", include("myapp.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

