from django.contrib import admin
from .models import ReviewModel, ShoppingMediaModel, ShoppingCartModel, PurchaseHistoryModel

# Register your models here.

admin.site.register(ReviewModel)

admin.site.register(ShoppingMediaModel)

admin.site.register(ShoppingCartModel)

admin.site.register(PurchaseHistoryModel)
