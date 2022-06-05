from django.contrib import admin

# Register your models here.
from .models import Client, Logement, Visite, Vente

class AuthorAdmin(admin.ModelAdmin):
    pass
admin.site.register(Client, AuthorAdmin)
admin.site.register(Logement, AuthorAdmin)
admin.site.register(Visite, AuthorAdmin)
admin.site.register(Vente, AuthorAdmin)
