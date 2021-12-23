from django.contrib import admin
from Person.models import Person


# Register your models here.
class PersonAdmin(admin.ModelAdmin):
    readonly_fields = ('city', 'zip', 'state', 'country')


admin.site.register(Person,PersonAdmin)
