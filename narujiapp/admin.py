from django.contrib import admin
from .models import MyModel, AnotherModel

@admin.register(MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'age', 'birth_date', 'email', 'is_active', 'related_model')

@admin.register(AnotherModel)
class AnotherModelAdmin(admin.ModelAdmin):
    list_display = ('title',)
