from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from mainsite.models import Post, AccessInfo, Branch, StoreIncome, text1, City, Keep, Human, Adopt, Died

class PostAdmin(ImportExportModelAdmin):
    list_display = ('title', 'slug', 'pub_date')

admin.site.register(Post, PostAdmin)

admin.site.register(AccessInfo)

class BranchAdmin(admin.ModelAdmin):
    list_display = ('title', 'name')
admin.site.register(Branch, BranchAdmin)

class StoreIncomeAdmin(admin.ModelAdmin):
    list_display = ('branch', 'income_year',
    'income_month', 'income')

admin.site.register(StoreIncome, StoreIncomeAdmin)

class text1Admin(ImportExportModelAdmin):
    list_display = ('title', 'slug', 'pub_date')
admin.site.register(text1, text1Admin)

class CityAdmin(ImportExportModelAdmin):
    list_display = ('cityname', 'cityleader')
admin.site.register(City, CityAdmin)

class KeepAdmin(ImportExportModelAdmin):
    list_display = ('city', 'keep_year', 'keep_num')
admin.site.register(Keep, KeepAdmin)

class HumanAdmin(ImportExportModelAdmin):
    list_display = ('city', 'human_year', 'human_num')
admin.site.register(Human, HumanAdmin)

class AdoptAdmin(ImportExportModelAdmin):
    list_display = ('city', 'adopt_year', 'adopt_num')
admin.site.register(Adopt, AdoptAdmin)

class DiedAdmin(ImportExportModelAdmin):
    list_display = ('city', 'died_year', 'died_num')
admin.site.register(Died, DiedAdmin)