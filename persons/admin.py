from django.contrib import admin
from .models import Person



class PersonAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'age', 'email', 'house_address', )
    list_display_links = ('first_name',)
    list_filter = ('first_name', 'last_name', 'email', )


admin.site.register(Person, PersonAdmin)