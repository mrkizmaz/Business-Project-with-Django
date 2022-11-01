from django.contrib import admin
from .models import Business, Employers

# Register your models here.

admin.site.register(Employers)

@admin.register(Business)
class Business_Admin(admin.ModelAdmin):
    list_display = ["position", "company", "location", "published_date"]
    search_fields = ["position"]
    list_filter = ["published_date"]

    class Meta:
        model = Business
