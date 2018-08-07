from django.contrib import admin

# Register your models here.
from .models import Character, Moveset

class MovesetInline(admin.TabularInline):
    model = Moveset
    extra = 23

class CharacterAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Name',                  {'fields': ['name']}),
        ('Date Published',        {'fields': ['pub_date']}),
    ]
    inlines = [MovesetInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

admin.site.register(Character, CharacterAdmin)
