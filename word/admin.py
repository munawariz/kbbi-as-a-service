from django.contrib import admin
from word.models import Word, Meaning

@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    pass

@admin.register(Meaning)
class MeaningAdmin(admin.ModelAdmin):
    pass
