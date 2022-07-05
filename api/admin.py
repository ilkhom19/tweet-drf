from django.contrib import admin
from .models import Author, Tweet

admin.site.register(Author)
admin.site.register(Tweet)