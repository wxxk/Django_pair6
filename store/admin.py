from django.contrib import admin
from accounts.models import User
from store.models import Store

# Register your models here.

admin.site.register(User)
admin.site.register(Store)
