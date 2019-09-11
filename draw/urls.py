# chat/urls.py
from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path('voteLarge/', views.voteLarge, name='voteLarge'),
    path('voteSmall/', views.voteSmall, name='voteSmall'),
    path('voteSmallTEST/', views.voteSmallTEST, name='voteSmallTEST'),
    path('voteWinner/', views.voteWinner, name='voteWinner'),
    path('voteSmallConfirmation/', views.voteSmallConfirmation, name='voteSmallConfirmation'),
    path('wst/', views.wst, name='wst'),
] 

