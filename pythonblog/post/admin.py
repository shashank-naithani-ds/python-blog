from django.contrib import admin
from .models import Article
# Register your models here.
class ArticleAdmin(admin.ModelAdmin):
  list_display = ("title", "slug", "status", "date",)
  # prepopulated_fields adds needed js to prepopulate the slug input automatically
  prepopulated_fields = {'slug': ('title',)}
admin.site.register(Article, ArticleAdmin)