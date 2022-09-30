from django.contrib import admin

from users.models import User


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk',
                    'username',
                    'email',
                    'first_name',
                    'last_name',
                    'is_staff',
                    'is_active',
                    )
    list_editable = ('username',
                     'email',
                     'first_name',
                     'last_name',
                     'is_staff',
                     'is_active',
                     )
    search_fields = ('username',
                     'email',
                     'first_name',
                     'last_name',
                     )
    list_filter = ('is_staff',
                   'is_active',
                   )
    empty_value_display = 'empty'


admin.site.register(User, UserAdmin)
