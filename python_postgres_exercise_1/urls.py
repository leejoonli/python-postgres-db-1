from django.urls import path
from . import views

urlpatterns = [
    path('regions/', views.RegionList.as_view(), name='region_list'),
    path('regions/<int:pk>', views.RegionDetail.as_view(), name='region_detail'),
    path('countries/', views.CountryList.as_view(), name='country_list'),
    path('countries/<int:pk>', views.CountryDetail.as_view(), name='country_detail'),
    path('locations/', views.LocationList.as_view(), name='location_list'),
    path('locations/<int:pk>', views.LocationDetail.as_view(), name='location_detail'),
    path('departments/', views.DepartmentList.as_view(), name='departments_list'),
    path('departments/<int:pk>', views.DepartmentDetail.as_view(), name='departments_detail'),
    path('jobs/', views.JobList.as_view(), name='jobs_list'),
    path('jobs/<int:pk>', views.JobDetail.as_view(), name='jobs_detail'),
]