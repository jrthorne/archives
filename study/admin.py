###################################################################
FileName        = 'admin.py'
# By:            Nan JIN
# Date:            30-06-2015
# Description:     The archeologist project - Usability Testing
##################################################################
from study.models import *

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

admin.site.register(survey)
admin.site.register(question)
admin.site.register(questionChoice)
admin.site.register(participant)
admin.site.register(choiceAnswer)
admin.site.register(freeAnswer)