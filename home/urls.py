from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.sign_in, name='login'),
    # path('logout/', views.sign_out, name='logout'),
    path('secret/', views.secret, name='secret'),
    path('ajax/', views.ajax, name='ajax'),
]
