from django.urls import path
from . import views

urlpatterns = [
    path('showstock', views.show_stock, name='showstock'),
]