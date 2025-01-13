from django.urls import path,re_path
from django.views.generic import RedirectView
from django.conf import settings
from django.views.static import serve

from .views import *

urlpatterns = [
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('',view=home,name="home"),
    path('join',view=join,name="join room"),
    path('create',view=create,name="create room"),
    path('game',view=gamewindow,name="game start"),
    path('signup',view=signup_player,name="add user"),
    path('login',view=login_player,name="login user"),
    path('logout',view=logout_player,name="logout user"),
    path('accounts/login/',RedirectView.as_view(url='/login', permanent=True)),
]