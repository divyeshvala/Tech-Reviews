from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', views.products_view, name = "products_view_url"),
    path('reviews/<p_id>', views.display_view, name="display_view_url"),
    path('reviews/<p_id>/write', views.write_view),
]

urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)