from django.contrib import admin
from subcribers.models import *
from wagtail.contrib.modeladmin.options import (
    ModelAdmin, 
    modeladmin_register,
)

# # Register your models here.
class SubcriberAdmin(ModelAdmin):

    model = Subcriber
    menu_label = 'Subscribers'
    menu_icon = "placholder"
    menu_order = 290
    add_to_setting_menu = False
    exclude_from_explorer = False
    list_display = ("full_name","email",)
    search_fields = ("full_name","email",)

modeladmin_register(SubcriberAdmin)
