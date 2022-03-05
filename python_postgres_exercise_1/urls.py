from django.urls import path
from . import views

urlpatterns = [
    path('regions/', views.RegionList.as_view(), name='region_list'),
    path('regions/<int:pk>', views.RegionDetail.as_view(), name='region_detail'),
]