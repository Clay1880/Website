from django.contrib import admin
from home.models import Contact
from home.models import PistolOrder
from home.models import RiflesOrder
from home.models import ShotgunOrder
from home.models import SniperOrder
from home.models import SubMachineOrder


# Register your models here.
admin.site.register(Contact)
admin.site.register(PistolOrder)
admin.site.register(RiflesOrder)
admin.site.register(ShotgunOrder)
admin.site.register(SniperOrder)
admin.site.register(SubMachineOrder)
