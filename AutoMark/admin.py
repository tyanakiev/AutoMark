from django.contrib import admin
from AutoMark.models import InstagramAccount, InstagramSettings, InstagramCeleryTask


# Register your models here.
admin.site.register(InstagramAccount)
admin.site.register(InstagramSettings)
admin.site.register(InstagramCeleryTask)

