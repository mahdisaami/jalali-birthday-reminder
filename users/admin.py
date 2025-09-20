
from users.models import Birthday, CustomUser
from django.contrib import admin

#from django_jalali.admin.filters import JDateFieldListFilter
#import django_jalali.admin as jadmin

@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('username','first_name','last_name' , 'gender', 'national_code', 'birthday_date')
    search_fields = ('username','full_name')
    list_filter = ('country', 'gender')
    ordering = ('ceremony_datetime',)

    def first_name(self, obj):
        fullname = obj.get_first_and_last_name()
        return fullname['first_name']
    def last_name(self, obj):
        fullname = obj.get_first_and_last_name()
        return fullname['last_name']

    first_name.admin_order_field = 'full_name'
    last_name.admin_order_field = 'full_name'


admin.site.register(Birthday)


