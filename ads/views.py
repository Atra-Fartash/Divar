from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404
from ads.models import Category, Ad

def all_ads(request):
    ads = Ad.objects.all().values('title', 'price', 'area')
    ads = list(ads)
    return JsonResponse(ads, safe=False)

def all_categories(request, category_name):
    category = get_object_or_404(Category,title__iexact = category_name)
    ads = Ad.objects.filter(category_id =category.id).values('title')
    ads = list(ads)
    return JsonResponse(ads, safe=False)

def City(request, city_name):
    ads = Ad.objects.filter(city__name__iexact = city_name).values('title', 'price', 'area')
    ads = list(ads)
    return JsonResponse(ads, safe=False)

def delete_ads(request, ad_id):
    ads = get_object_or_404(Ad, id = ad_id)
    ads.delete()
    return HttpResponse("Product Deleted")
