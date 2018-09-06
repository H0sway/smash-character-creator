# Import Modules
from django.urls import path, re_path
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Urls for the server
urlpatterns = [
    path('admin/', admin.site.urls),
    re_path('api/characters/', views.CharacterListCreate.as_view()),
    re_path('api/characters/<int:pk>', views.CharacterDetail.as_view()),
    re_path('api/moveset/', views.MovesetListCreate.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
