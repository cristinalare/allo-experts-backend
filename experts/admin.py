from django.contrib import admin
from .models import Expert



class ExpertModelAdmin(admin.ModelAdmin):
  def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["slug"].help_text = "This field is automatically generated"
        return form
  
admin.site.register(Expert, ExpertModelAdmin)