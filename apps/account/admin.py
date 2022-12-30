from django.contrib import admin
from apps.account.models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'middle_name', 'email', 'phone', 'date_created', 'is_active')
    readonly_fields = ('date_modified', 'date_created')
    search_fields = ('id', 'name', 'surname', 'middle_name', 'email', 'phone')


admin.site.register(Account, AccountAdmin)
