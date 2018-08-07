# Import Modules
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Urls for the server
urlpatterns = [
    path('characters/', views.CharacterListCreate.as_view()),
    path('moveset/', views.MovesetListCreate.as_view()),
] # + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
