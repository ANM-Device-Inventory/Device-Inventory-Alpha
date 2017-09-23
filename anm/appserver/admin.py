from django.contrib import admin

# Register your models here.
from .models import NIC,HD,CPU

admin.site.register(NIC);
admin.site.register(HD);
admin.site.register(CPU);