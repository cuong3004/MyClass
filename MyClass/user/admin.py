from django.contrib import admin
from .models import Class_User, Image_User

# Register your models here.
class UserAdmin(admin.ModelAdmin):
	list_display = ['full_name', 'image_rep']

admin.site.register(Class_User, UserAdmin)
admin.site.register(Image_User)