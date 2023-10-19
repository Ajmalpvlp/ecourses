from django.contrib import admin
from .models import Member
# Register your models here.
@admin.register(Member)
class Member(admin.ModelAdmin):
    list_display= ('id', 'name', 'course', 'parent', 'adrs', 'district', 'tel')