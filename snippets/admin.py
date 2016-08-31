from django.contrib import admin
from snippets.models import Snippet

# Register your models here.

class SnippetsAdmin(admin.ModelAdmin):
	list_display = ('created','title','code','linenos','language','style')

admin.site.register(Snippet, SnippetsAdmin)
