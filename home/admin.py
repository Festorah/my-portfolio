from django.contrib import admin
from .models import Contact

admin.site.site_header = "Muchmore"


admin.site.register(Contact)
