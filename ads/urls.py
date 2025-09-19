from django.urls import path
from ads.views import (
    all_ads,
    all_categories,
    delete_ads,
    City
    )

urlpatterns = [
    path('ads/', all_ads),
    path('categories/<str:category_name>/', all_categories),
    path('delete-ad/<int:ad_id>/', delete_ads),
    path('<str:city_name>/', City),
]