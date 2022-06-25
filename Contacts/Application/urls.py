from django.urls import path
from . import views

urlpatterns = [
    path('accueil', views.accueil, name='accueil'),
    path('contact/<str:pk>/', views.contact, name="contact"),
    path('creer', views.creer, name="creer_co"),
    path('modifier/<str:pk>/', views.modifier, name='modif_co'),
    path('supprimer/<str:pk>/', views.supprimer, name='supp_co'),
]