from django.contrib import admin

# Register your models here.
from .models import Users
from .models import UplodedItems
admin.site.register(Users)
admin.site.register(UplodedItems)