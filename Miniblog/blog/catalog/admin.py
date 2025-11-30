from django.contrib import admin
from .models import Blog, Author, Comment

# Register your models here.
#admin.site.register(Blog)
admin.site.register(Author)
admin.site.register(Comment)



@admin.register(Blog)
class BlogAdmin (admin.ModelAdmin):
    list_display = ('title', 'author','pub_date') 