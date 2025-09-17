from django.urls import path
from ads.views import (
    all_ads,
    all_categories,
    delete_ads, City
    )

urlpatterns = [
    path('ads', all_ads),
    path('all-categories', all_categories),
    path('delete-ad/<int:id>', delete_ads),
    path('city/<slug:city>', City),
]