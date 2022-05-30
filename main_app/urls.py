from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('cards/', views.cards_index, name='index'),
    path('cards/<int:card_id>/', views.card_details, name='detail'),
    path('cards/create/', views.CardCreate.as_view(), name='cards_create'),
    path('cards/<int:pk>/update/', views.CardUpdate.as_view(), name='cards_update'),
    path('cards/<int:pk>/delete/', views.CardDelete.as_view(), name='cards_delete'),
    path('cards/<int:card_id>/add_copies/', views.add_copies, name='add_copies'),
    path('cards/<int:card_id>/assoc_effect/<int:effect_id>/', views.assoc_effect, name='assoc_effect'),
    path('cards/<int:card_id>/disassoc_effect/<int:effect_id>/', views.disassoc_effect, name='disassoc_effect'),
    path('effects/', views.EffectList.as_view(), name='effect_index'),
    path('effects/<int:pk>/', views.EffectDetail.as_view(), name='effect_detail'),
    path('effects/create/', views.EffectCreate.as_view(), name='effect_create'),
    path('effects/<int:pk>/update/', views.EffectUpdate.as_view(), name='effect_update'),
    path('effects/<int:pk>/delete/', views.EffectDelete.as_view(), name='effect_delete'),
    path('accounts/signup/', views.signup, name='signup'),
]
