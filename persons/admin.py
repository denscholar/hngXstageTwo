from django.contrib import admin
from .models import Person



class PersonAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email', 'house_address', )
    list_display_links = ('name',)
    list_filter = ('name', 'email', )


admin.site.register(Person, PersonAdmin)