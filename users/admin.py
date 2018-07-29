from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin

User = get_user_model()


class CustomUserAdmin(UserAdmin):
    list_display = [
        'email',
        'role',
        'first_name',
        'last_name',

    ]

    list_filter = ('role',)

    fieldsets = (
                (None, {'fields': ('email', 'password')}),
                ('Personal info', {
                 'fields': (
                     # 'avatar',
                     'first_name',
                     'last_name',
                     # 'middle_name',
                     # 'phone',
                     # 'skype',
                 )}),
                ('Professional info', {
                    'fields': (
                        # 'address',
                        # 'specialization',
                        # 'extra',
                        # 'about_self',
                        # 'video',
                    )
                }),
                ('Permissions', {'fields': ('is_staff', 'role')}),
                ('Important dates', {'fields': ('last_login', 'is_active', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': (
                'email',
                'role',
                'password1',
                'password2'
            )}
         ),
    )

    search_fields = ('email',)
    ordering = ('email',)
    filter_horizontal = ()


admin.site.register(User, CustomUserAdmin)
