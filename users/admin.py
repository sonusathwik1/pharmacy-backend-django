from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Role, UserProfile


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ("name", "description")
    search_fields = ("name",)


class UserProfileInline(admin.StackedInline):
    model = UserProfile
    can_delete = False
    extra = 0
    max_num = 1   # ⛔ absolutely no new rows
    fields = ("role", "store", "phone_number")

    def has_add_permission(self, request, obj=None):
        # ⛔ prevent admin from creating UserProfile
        return False

    def get_readonly_fields(self, request, obj=None):
        if not request.user.is_superuser:
            return ("role",)
        return ()


class UserAdmin(BaseUserAdmin):
    def get_inline_instances(self, request, obj=None):
        # Show inline ONLY on edit page
        if obj is None:
            return []
        return [UserProfileInline(self.model, self.admin_site)]

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        if request.user.is_superuser:
            return qs
        return qs.filter(is_staff=True)


admin.site.unregister(User)
admin.site.register(User, UserAdmin)


@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("user", "role", "store")
    list_filter = ("role", "store")
    search_fields = ("user__username",)
