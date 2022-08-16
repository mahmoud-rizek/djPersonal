from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import posts

# Register your models here.
# Apply summernote to all TextField in model.
class postModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
 
admin.site.register(posts, postModelAdmin)
