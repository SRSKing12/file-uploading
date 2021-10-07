from django.urls import path
from fl import views
from django.conf.urls.static import static
from django.conf import settings
from .views import DelFile

urlpatterns = [
    path('', views.index, name="index"),
    path('download', views.download, name="download"),
    path('delete-file/<int:pk>', DelFile.as_view(), name="delete-file"),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)