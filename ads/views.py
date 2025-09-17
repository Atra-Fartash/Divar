from django.http import HttpResponse, JsonResponse
from ads.models import Category, Ad

def all_ads(request):
    ads = Ad.objects.all().values('title', 'price', 'area')
    ads = list(ads)
    return JsonResponse(ads, safe=False)

def all_categories(request):
    categories = Category.objects.all().values('name')
    categories = list(categories)
    return JsonResponse(categories, safe=False)

def City(request, city):
    ads = Ad.objects.filter(city = city).values('title')
    ads = list(ads)
    return JsonResponse(ads, safe=False)

def delete_ads(request, id):
    Ad.objects.get(id = id).delete()
    return HttpResponse("Product Deleted")
