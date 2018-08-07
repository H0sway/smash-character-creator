# Import Modules
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Urls for the server
urlpatterns = [
    path('api/characters/', views.CharacterListCreate.as_view()),
    path('api/neutralattack/', views.CharacterListCreate.as_view()),
    path('api/forwardtilt/', views.ForwardTiltListCreate.as_view()),
    path('api/uptilt/', views.UpTiltListCreate.as_view()),
    path('api/downtilt/', views.DownTiltListCreate.as_view()),
    path('api/forwardsmash/', views.ForwardSmashListCreate.as_view()),
    path('api/upsmash/', views.UpSmashListCreate.as_view()),
    path('api/downsmash/', views.DownSmashListCreate.as_view()),
    path('api/dashattack/', views.DashAttackListCreate.as_view()),
    path('api/forwardarial/', views.ForwardArialListCreate.as_view()),
    path('api/backwardarial/', views.BackwardArialListCreate.as_view()),
    path('api/uparial/', views.UpArialListCreate.as_view()),
    path('api/downarial/', views.DownArialListCreate.as_view()),
    path('api/forwardthrow/', views.ForwardThrowListCreate.as_view()),
    path('api/backwardthrow/', views.BackwardThrowListCreate.as_view()),
    path('api/upthrow/', views.UpThrowListCreate.as_view()),
    path('api/downthrow/', views.DownThrowListCreate.as_view()),
    path('api/neutralspecial/', views.NeutralSpecialSerializer.as_view()),
    path('api/sidespecial/', views.SideSpecialSerializer.as_view()),
    path('api/upspecial/', views.UpSpecialListCreate.as_view()),
    path('api/downspecial/', views.DownSpecialListCreate.as_view()),
    path('api/finalsmash/', views.FinalSmashListCreate.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
