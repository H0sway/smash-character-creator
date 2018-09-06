from django.contrib import admin

# Register your models here.
from .models import Character, Moveset

class MovesetInline(admin.TabularInline):
    model = Moveset
    extra = 23

class CharacterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',                  {'fields': ['name']}),
        ('Series',                {'fields': ['series']}),
        ('Description',           {'fields': ['description']}),
        ('Character Image',       {'fields': ['char_image']})
    ]
    inlines = [MovesetInline]
    list_display = ('name', 'pub_date')
    list_filter = ['pub_date']
    search_fields = ['name', 'series']

admin.site.register(Character, CharacterAdmin)
