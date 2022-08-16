from django.contrib import admin
from .models import about
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class aboutModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
 
admin.site.register(about, aboutModelAdmin)
