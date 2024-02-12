from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path('',views.home,name='home'),
    path('profile/<str:unique_id>',views.profile,name='profile'),
    path('modal/<str:unique_id>',views.modal,name='modal'),
]


urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
