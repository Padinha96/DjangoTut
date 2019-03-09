from tinymce.widgets import TinyMCE
from django.contrib import admin
from django.db import models
from .models import Tutorial, TutorialSeries, TutorialCategory
# Register your models here.

class TutorialAdmin(admin.ModelAdmin):

    fieldsets = [
        ("Title/Date", {"fields": ["title", "published"]}),
        ("URL", {"fields": ["slug"]}),
        ("Series", {"fields": ["series"]}),
        ("Content", {"fields": ["content"]})
    ]

    formfield_overrides = {
        models.TextField: {'widget' : TinyMCE()}
    }

admin.site.register(TutorialSeries)

admin.site.register(TutorialCategory)


admin.site.register(Tutorial, TutorialAdmin)
