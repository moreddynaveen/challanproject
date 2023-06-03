from django.contrib import admin
from app1.models import Challan
class Challanadmin(admin.ModelAdmin):
    list_display=('id','sno','vehicle','date','amount')
admin.site.register(Challan,Challanadmin)
# Register your models here.
