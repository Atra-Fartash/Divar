from django.contrib import admin
from ads.models import User, Category, Ad, City, Area, Reports, Payment, Message


class AdAdmin(admin.ModelAdmin):
    list_display = ['title', 'price']
    search_fields = ['title']
    list_filter = ['category']


admin.site.register(User)
admin.site.register(Category)
admin.site.register(City)
admin.site.register(Ad, AdAdmin)
admin.site.register(Area)
admin.site.register(Reports)
admin.site.register(Payment)
admin.site.register(Message)