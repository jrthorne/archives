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
class ChoiceInline(admin.TabularInline):
    model = choice
    extra = 0

# end ChoiceInline

##################################################################
class QuestionAdmin(admin.ModelAdmin):
    fieldsets   = [ (None,               {'fields': ['questionText']}),
                   (None,               {'fields': ['survey']}),
                   (None,               {'fields': ['type']}),
                   ]
    
    inlines     = [ChoiceInline]
    list_display= ('survey','questionText')
    list_filter = ['survey']
    search_fields = ['questionText']

# end QuestionAdmin

##################################################################
class ChoiceAdmin(admin.ModelAdmin):
    list_display= ('survey','question','choiceText')
    list_filter = ['choiceText']
    search_fields = ['choiceText']

# end ChoiceAdmin

##################################################################
class ParticipantAdmin(admin.ModelAdmin):
    list_display= ('registerNumber','historicalSite','task','entered')
    list_filter = ['registerNumber']
    search_fields = ['registerNumber','historicalSite','task']

# end ChoiceAdmin

##################################################################

admin.site.register(survey)
admin.site.register(question, QuestionAdmin)
admin.site.register(choice, ChoiceAdmin)
admin.site.register(participant,ParticipantAdmin)
admin.site.register(choiceAnswer)
admin.site.register(freeAnswer)
admin.site.register(map)
