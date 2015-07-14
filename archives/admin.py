###################################################################
FileName        = 'admin.py'
# By:            Jason Thorne
# Date:            11-03-2012
# Description:     The archeologist project
##################################################################
from archives.models import *

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
# r50
from django import forms
##################################################################
class relicAdmin(admin.ModelAdmin):
    list_display        = ['id', 'name', 'historical_site', 'photo']
    list_filter            = ['historical_site']
# end relicAdmin

##################################################################

admin.site.register(archeologist)
admin.site.register(period)
admin.site.register(historical_site)
admin.site.register(relic_type)
admin.site.register(relic, relicAdmin)

