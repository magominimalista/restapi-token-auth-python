from django.contrib import admin
from .models import Register


class RegisterAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'address', 'phone', 'date')
    verbose_name = 'General register'
    name = 'register'
    search_fields = ('name', 'email')
    list_filter = ('date',)

admin.site.register(Register, RegisterAdmin)
