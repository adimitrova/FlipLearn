from django.contrib import admin
from .models import Card, Tag, User

# Register your models here.

admin.site.register(User)
admin.site.register(Card)
admin.site.register(Tag)
