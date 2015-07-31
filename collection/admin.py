from django.contrib import admin
from django.core.urlresolvers import reverse

from .models import Mineral, Image

class ImageAdmin(admin.TabularInline):
    model = Image

class MineralAdmin(admin.ModelAdmin):
    inlines = [
            ImageAdmin
    ]

    def view_on_site(self, obj):
        return reverse('detail', kwargs={'mineral_id': obj.id})


admin.site.register(Mineral, MineralAdmin)
