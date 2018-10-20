
# Register your models here.
from django.contrib import admin
from .models import Theory_Assignment,Lab_Assignment,Theory_Lectures,Lab_Lectures
# Register your models here.
admin.site.register(Theory_Assignment)
admin.site.register(Lab_Assignment)
admin.site.register(Theory_Lectures)
admin.site.register(Lab_Lectures)

