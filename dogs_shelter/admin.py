from django.contrib import admin

from .models import Dog, Curator, Breed, Payment

admin.site.register(Dog)
admin.site.register(Curator)
admin.site.register(Breed)
admin.site.register(Payment)
