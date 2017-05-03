from django.contrib import admin

from .models import Run



class RunAdmin(admin.ModelAdmin):
    fieldsets = [
             (None,               {'fields': ['distance']}),
             ('Date information', {'fields': ['run_date']}),
                ]



admin.site.register(Run, RunAdmin)