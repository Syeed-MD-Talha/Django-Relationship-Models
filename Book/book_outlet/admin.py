from django.contrib import admin
from . models import Booklist,Author,Address,Country
# Register your models here.

class BooklistAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('title',)}
    list_display=('id','title','rating','is_bestSelling','author','get_published_countries')

class AuthorAdmin(admin.ModelAdmin):
    list_display=('first_name','last_name')

class AddressAdmin(admin.ModelAdmin):
    list_display=('street','postal_code','city')

class CountryAdmin(admin.ModelAdmin):
    list_display=('country_name','country_code')

admin.site.register(Booklist,BooklistAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Address,AddressAdmin)
admin.site.register(Country,CountryAdmin)