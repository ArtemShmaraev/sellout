from django.contrib import admin

# Register your models here.
from .models import Product, Category, Tag, Brand, Gender, Collection, Color, Line, SizeTable, SizeTranslationRows


class ProductAdmin(admin.ModelAdmin):
    list_display = ('model', '_brand', 'colorway', '_line', 'min_price')
    search_fields = ("brands__name", "model", "colorway", "lines__name")

    # prepopulated_fields = {'slug': ('name',)}

    def _brand(self, row):
        return ','.join([x.name for x in row.brands.all()])

    def _line(self, row):
        return ','.join([x.name for x in row.lines.all()])


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('full_name',)


class LineAdmin(admin.ModelAdmin):
    list_display = ('full_name', "full_eng_name")


class ColorAdmin(admin.ModelAdmin):
    list_display = ('name',)


class BrandAdmin(admin.ModelAdmin):
    list_display = ('name',)


class GenderAdmin(admin.ModelAdmin):
    list_display = ('name',)


class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)


class CollectionAdmin(admin.ModelAdmin):
    list_display = ('name',)


# class SizeAdmin(admin.ModelAdmin):
#     list_display = ('INT',)

class SizeRowsAdmin(admin.ModelAdmin):
    list_display = ('US',)


class SizeTableAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'category', 'gender')


admin.site.register(Product, ProductAdmin)
admin.site.register(Brand, BrandAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Gender, GenderAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Color, ColorAdmin)
admin.site.register(Line, LineAdmin)
admin.site.register(SizeTable, SizeTableAdmin)
admin.site.register(SizeTranslationRows, SizeRowsAdmin)
