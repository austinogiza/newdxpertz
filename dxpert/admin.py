from django.contrib import admin

# Register your models here.

from . models import Contact, Courses


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'phone', 'message')


admin.site.register(Contact, ContactAdmin)
admin.site.register(Courses)
