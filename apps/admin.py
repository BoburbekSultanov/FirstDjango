from django.contrib import admin

from apps.models import Jobs


# Register your models here.

@admin.register(Jobs)
class JobsAdmin(admin.ModelAdmin):
    pass
