from django.contrib import admin
from .models  import *
# Register your models here.
@admin.register(RegisterModel)
class RegisterAdmin(admin.ModelAdmin):
    list_display=['fullname','username','email','password','confirm_password','mobile']



