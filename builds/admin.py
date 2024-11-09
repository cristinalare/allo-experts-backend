from django.contrib import admin
from .models import Build
from django.urls import path
from django.shortcuts import render
from core.admin import GraphAdmin
from django.utils.html import format_html

class BuildModelAdmin(GraphAdmin):
  filter_horizontal = ('mechanisms', 'courses', 'experts', 'builds')

  def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request, obj=obj, change=change, **kwargs)
        form.base_fields["slug"].help_text = "This field is automatically generated"
        return form
  
  list_display = ('title', 'created_at', 'slug', 'view_on_site_link')
  search_fields = ('title', 'description', 'slug')

  def view_on_site_link(self, obj):
        return format_html('<a href="{}" target="_blank">View on allo.expert</a>', obj.get_absolute_url())
  view_on_site_link.short_description = 'allo.expert link'

  def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('network/<int:object_id>/', self.admin_site.admin_view(self.network_view), name='build_network'),
        ]
        return custom_urls + urls

  def network_view(self, request, object_id):
        instance = self.get_object(request, object_id)
        related_data = self.get_related_data(instance)
        return render(request, 'core/change_form.html', {
            'data': related_data,
            'original': instance,
            'graph_script': self.get_graph_script(related_data),
        })
  
admin.site.register(Build, BuildModelAdmin)

