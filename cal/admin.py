from django.contrib import admin
from .models import item_preparation_detail, factorylog, note, item, worker

admin.site.register(item_preparation_detail)
admin.site.register(factorylog)
admin.site.register(note)
admin.site.register(item)
admin.site.register(worker)


# Register your models here.
