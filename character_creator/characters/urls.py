# Import Modules
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

# Urls for the server
urlpatterns = [
    path('characters/', views.CharacterListCreate.as_view()),
    path('neutralattack/', views.CharacterListCreate.as_view()),
    path('forwardtilt/', views.ForwardTiltListCreate.as_view()),
    path('uptilt/', views.UpTiltListCreate.as_view()),
    path('downtilt/', views.DownTiltListCreate.as_view()),
    path('forwardsmash/', views.ForwardSmashListCreate.as_view()),
    path('upsmash/', views.UpSmashListCreate.as_view()),
    path('downsmash/', views.DownSmashListCreate.as_view()),
    path('dashattack/', views.DashAttackListCreate.as_view()),
    path('forwardarial/', views.ForwardArialListCreate.as_view()),
    path('backwardarial/', views.BackwardArialListCreate.as_view()),
    path('uparial/', views.UpArialListCreate.as_view()),
    path('downarial/', views.DownArialListCreate.as_view()),
    path('forwardthrow/', views.ForwardThrowListCreate.as_view()),
    path('backwardthrow/', views.BackwardThrowListCreate.as_view()),
    path('upthrow/', views.UpThrowListCreate.as_view()),
    path('downthrow/', views.DownThrowListCreate.as_view()),
    path('neutralspecial/', views.NeutralSpecialListCreate.as_view()),
    path('sidespecial/', views.SideSpecialListCreate.as_view()),
    path('upspecial/', views.UpSpecialListCreate.as_view()),
    path('downspecial/', views.DownSpecialListCreate.as_view()),
    path('finalsmash/', views.FinalSmashListCreate.as_view()),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
