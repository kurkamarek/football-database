from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hraci/', views.HracListView.as_view(), name='hraci'),
    path('hraci/<int:pk>', views.HracDetailView.as_view(), name='hraci_detail'),
]