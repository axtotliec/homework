from django.contrib import admin
# Import and Export
from import_export.admin import ImportExportModelAdmin
from import_export import resources

#Import models
from .models import Category, Tableone, Tabletwo, Tablethree

class CategoryResource(resources.ModelResource):
    class Meta:
        model = Category

class TableoneResource(resources.ModelResource):
    class Meta:
        model = Tableone

class TabletwoResource(resources.ModelResource):
    class Meta:
        model = Tabletwo

class TablethreeResource(resources.ModelResource):
    class Meta:
        model = Tablethree

class CategoryAdmin(ImportExportModelAdmin):
    resource_class = CategoryResource

class TableoneAdmin(ImportExportModelAdmin):
    resource_class = TableoneResource

class TabletwoAdmin(ImportExportModelAdmin):
    resource_class = TabletwoResource

class TablethreeAdmin(ImportExportModelAdmin):
    resource_class = TablethreeResource

# Register your models here.
admin.site.register(Category,CategoryAdmin) 
admin.site.register(Tableone, TableoneAdmin)
admin.site.register(Tabletwo, TabletwoAdmin)
admin.site.register(Tablethree, TablethreeAdmin)
