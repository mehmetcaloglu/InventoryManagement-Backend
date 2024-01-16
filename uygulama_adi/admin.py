# admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from uygulama_adi.models import UserProfile,Stock,Category,Depot,Order,Product,Sale,User # Replace 'your_app' with your actual app name


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    verbose_name_plural = 'UserProfile'

class UserAdmin(BaseUserAdmin):
    inlines = (UserProfileInline, )  # Bu satırı kaldırın


admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(UserProfile)
admin.site.register(Stock)
admin.site.register(Category)
admin.site.register(Depot)
admin.site.register(Order)
admin.site.register(Product)
admin.site.register(Sale)

