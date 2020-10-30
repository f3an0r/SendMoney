from django.contrib import admin
from distribution_money.models import User

# Register your models here.

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)
