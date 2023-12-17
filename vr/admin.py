from django.contrib import admin
from .models import VinanPetLtd, Branch, Product
from django.contrib.auth.models import Group
from import_export.admin import ImportExportModelAdmin

# Register your models here.

admin.site.site_header = 'Vinan Pet Ltd Dashboard'

class VinanpetLtdImportExportAdmin(ImportExportModelAdmin):
    pass

class VinanPetLtdAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    model = VinanPetLtd
     # list_display = ('transaction_Date', 'entry_Date', 'branch', 'product', 'tank_1_Opening', 'tank_1_Closing', 'tank_1_Difference', 'pump_1_Opening', 'pump_1_Closing', 'pump_1_Difference', 'price', 'expected_Cash', 'pos', 'expenses', 'balance', 'teller_ID', 'teller')
    list_display = [field.name for field in VinanPetLtd._meta.get_fields() if field.name not in ('id', 'created', 'modified', 'is_complete', 'session_key', 'multipagemodel_ptr')]
    list_filter = ['branch', 'transaction_Date']
    change_list_template = "admin/change_list.html"
    # change_list_template = "admin/change_list_filter_confirm.html"
    # change_list_template = "admin/change_list_filter_sidebar.html"
    # change_list_template = "admin/change_list_filter_confirm_sidebar.html"
    search_fields = ['branch__branch', 'transaction_Date']
    exclude = ('session_key',)


admin.site.register(VinanPetLtd, VinanPetLtdAdmin)
admin.site.register(Branch)
admin.site.register(Product)

admin.site.unregister(Group)